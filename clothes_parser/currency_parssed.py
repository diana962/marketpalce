from bs4 import BeautifulSoup import requests


def parser(url='https://www.akchabar.kg/ru/exchange-rates/'):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')  # lxml the most fast stuff
    countainer = soup.find('tbody')
    banks = countainer.find_all('tr')[:-1]
    result = []
    for bank in banks:
        title = bank.find_all('td')[0].find('a').get('title')
        dollar1 = bank.find_all('td')[1].text
        dollar2 = bank.find_all('td')[2].text

        data = {'title': title, 'dollar1': dollar1, 'dollar2': dollar2}
        result.append(data)
    return result
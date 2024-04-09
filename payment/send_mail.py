from decouple import config
from django.core.mail import send_mail


HOST = config('HOST')

def send_mail_payment(user):
    link = f'{HOST}/payments/'
    send_mail(
        'Hello, here is your pay-check',

        f'Check for the last purchase:\n\n{link}\n'

        f'\nHave a nice day!\n',

        f'dianataalaibekova2002@gmail.com',
        [user],
        fail_silently=False,
    )


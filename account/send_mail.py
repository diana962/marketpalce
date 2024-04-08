from decouple import config
from django.core.mail import send_mail

HOST = config('HOST')


def send_mail_register(user, code):
    link = f'{HOST}/accounts/activate/{code}/'
    send_mail(
        'Hello, please activate your account',

        f'To activate your account enter a link bellow: \n\n{link}\n'
        
        f'\nLink works only one time!\n',

        f'dianataalaibekova2002@gmail.com',
        [user],
        fail_silently=False,
    )

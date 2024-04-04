from decouple import config
from django.core.mail import send_mail


def send_mail_register(user, code):
    send_mail(
        'Здраствуйте, пожалуйста активируйте ваш аккаунт',
        f'Вот ваш токен{code}\nВведите его по ссылке\n\thttp://localhost:8000/api/v1/accounts/activate/',
        config('EMAIL_USER'),
        [user],
        fail_silently=False
    )
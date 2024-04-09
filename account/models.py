import uuid
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .managers import UserManager


class CustomUser(AbstractUser):
    email = models.EmailField(
        verbose_name='Email',
        help_text='example@gmail.com',
        unique=True
    )

    is_active = models.BooleanField(
        _("active"),
        default=False,
        help_text=_(
            "Designates whether this user should be treated as active. "
            "Unselect this instead of deleting accounts."
        ),
    )

    activation_code = models.CharField(max_length=50, unique=True, blank=True)
    objects = UserManager() #no need

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def save(self, *args, **kwargs):
        code = uuid.uuid4().hex
        self.activation_code = code
        if self.is_superuser:
            self.is_active = True
        super().save(*args, **kwargs)

    class Meta:
        verbose_name = 'Account'
        verbose_name_plural = 'Accounts'
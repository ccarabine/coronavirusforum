from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings


def createUser(sender, instance, created, **kwargs):
    if created:
        user1 = instance
        subject = 'Welcome to CoronaVirus Forum'
        message = 'Thank you for joining the CoronaVirus Forum'

        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [user1.email],
            fail_silently=False,
        )


post_save.connect(createUser, sender=User)

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from django.contrib.auth.models import User

from django.core.mail import send_mail
from django.conf import settings




def createUser(sender, instance, created, **kwargs):
    if created:
        user1 = instance
        print(user1)
        subject = 'Welcome to CoronaVirus Forum'
        message = 'We are glad you are here!'

        send_mail(
            subject,
            message,
            'projectckcabs@gmail.com',
            ['ccarabine12@gmail.com'],
            fail_silently=False,
        )



post_save.connect(createUser, sender=User)

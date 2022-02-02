# Imports
# 3rd party:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings

# Internal:
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def createUser(sender, instance, created, **kwargs):
    """
        Sends an email to the user when a user signs up
        Args:
            sender: sender
            instance: instance (user)
            created: created date
            **kwargs: **kwargs
        Returns:
            N/A
        """
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

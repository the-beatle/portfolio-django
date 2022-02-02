from django.db.models.signals import post_save
from django.dispatch import receiver

from contact.models import Contact


def send_email(sender, instance, **kwargs):
    instance.send_mail()


post_save.connect(send_email, sender=Contact)

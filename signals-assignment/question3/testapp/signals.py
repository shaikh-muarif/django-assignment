from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Person
from django.db import transaction

@receiver(post_save, sender=Person)
def my_signal_handler(sender, instance, created, **kwargs):
    print("Signal received!")
    # This will raise an exception
    raise Exception("Error in signal handler!")

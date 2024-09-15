import time
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Person

@receiver(post_save, sender=Person)
def my_signal_handler(sender, instance, created, **kwargs):
    print("Signal received!")
    time.sleep(5)
    print("Signal handler finished after 5 seconds.")

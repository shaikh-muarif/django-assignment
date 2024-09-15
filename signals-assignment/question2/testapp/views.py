import threading
from django.shortcuts import render
from django.http import HttpResponse
from .models import Person

def save_model_with_thread_info(request):
    current_thread = threading.current_thread().name
    print(f"Main thread before saving: {current_thread}")

    obj = Person.objects.create(name="muarif")

    print(f"Main thread after saving: {current_thread}")

    return HttpResponse(f"Model instance '{obj.name}' saved with ID {obj.id}. Thread: {current_thread}")

from django.shortcuts import render
from django.http import HttpResponse
from .models import Person

def save_model_instance(request):
    print("Saving model instance...")
    obj = Person.objects.create(name="muarif")
    print("Model instance saved!")
    return HttpResponse(f"Model instance '{obj.name}' saved with ID {obj.id}")


from django.shortcuts import render
from django.http import HttpResponse
from django.db import transaction
from .models import Person

def save_model_with_transaction(request):
    try:
        with transaction.atomic():
            print("saving model instance...")
            obj = Person.objects.create(name="muarif")
            print("model instance saved!")
        return HttpResponse(f"Model instance '{obj.name}' saved with ID {obj.id}.")
    except Exception as e:
        print("Transaction rolled back due to error:", e)
        return HttpResponse(f"Transaction failed: {e}", status=500)

from django.urls import path
from .views import save_model_with_transaction

urlpatterns = [
    path('person/', save_model_with_transaction),
]

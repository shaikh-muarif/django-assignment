from django.urls import path
from .views import save_model_instance

urlpatterns = [
    path('person/', save_model_instance),
]
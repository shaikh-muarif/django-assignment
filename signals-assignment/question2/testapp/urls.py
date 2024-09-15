from django.urls import path
from .views import save_model_with_thread_info

urlpatterns = [
    path('save-thread-info/', save_model_with_thread_info),
]

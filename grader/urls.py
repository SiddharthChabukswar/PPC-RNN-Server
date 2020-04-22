from django.urls import path
from .views import call_model

urlpatterns = [
    path('grade/', call_model.as_view()),
]

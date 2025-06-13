from django.urls import path
from .views import add_employee

urlpatterns = [
    path('add/', add_employee, name='add_employee'),
]

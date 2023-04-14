from django.urls import path
from .views import handle_click

urlpatterns = [
    path('', handle_click, name='handle_click'),  
]
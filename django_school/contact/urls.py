from django.urls import path, include
from .views import *

urlpatterns = [
    path('', ContactView.as_view(), name='contact'),
]
from django.shortcuts import render
from django.views.generic import CreateView

from .models import *
from .forms import *

class ContactView(CreateView):
    model = Contact
    form_class = ContactForm
    success_url = '/'

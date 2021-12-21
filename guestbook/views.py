from django.shortcuts import render
from .models import GuestBook
from django.views.generic import ListView
# Create your views here.

class GuestBookListView(ListView):
    model = GuestBook
    template_name = 'home.html'

from django.shortcuts import render
from django.views.generic import ListView
from .models import (
    FixVersion
)

class FixVersionView(ListView):
    model = FixVersion
    template_name = 'home.html'

from django.shortcuts import render
from rest_framework.decorators import api_view

# Create your views here.

def index(request):
    return render(request, "pages/index.html")
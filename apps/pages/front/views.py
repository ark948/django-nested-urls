from django.shortcuts import render

def index(request):
    return render(request, "pages/front/index.html")
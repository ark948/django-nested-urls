from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

# Create your views here.

@api_view(['GET'])
def index(request):
    return Response(
        {
            "api link": reverse("blog:api:index", request=request),
            "front link": "none"
        }
    )
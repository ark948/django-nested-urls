from django.urls import path, include
from .views import index

app_name = "front"
urlpatterns = [
    path("", index, name="index"),
]
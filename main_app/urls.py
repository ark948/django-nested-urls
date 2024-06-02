from django.urls import path, include
from .views import index

urlpatterns = [
    path("", index),
    path("pages/", include("apps.pages.urls")),
    path("blogs/", include("apps.blog.urls")),
]
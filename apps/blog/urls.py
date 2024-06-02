from django.urls import path, include
from .views import index

app_name = 'blog'
urlpatterns = [
    path("", index, name="index"),
    path("api/", include("apps.blog.api.urls")),
]
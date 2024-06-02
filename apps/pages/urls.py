from django.urls import path, include
from .views import index

app_name = 'pages'
urlpatterns = [
    path("", index, name="index"),
    path("api/", include("apps.pages.api.urls")),
    path("front/", include("apps.pages.front.urls")),
]
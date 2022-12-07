from django.urls import path
from . import views


urlpatterns = [
    path("", views.main),
    path("options", views.option, name="options")
]
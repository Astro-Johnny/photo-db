from django.urls import path
from . import views


urlpatterns = [
    path("", views.main),
    path("camera/<int:id>", views.camera, name="camera"),
    path("film/<int:id>", views.film, name="film"),
    path("event/<int:id>", views.event, name="events"),
    path("options", views.option, name="options")
]
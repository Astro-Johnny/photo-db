from django.conf.urls.static import static
from django.conf import settings
from django.urls import path
from . import views


urlpatterns = [
    path("", views.main, name="main"),
    path("options", views.option, name="options"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
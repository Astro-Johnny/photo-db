from photos.tools.utility import getTableData, cameraId, filmId, eventId
from django.shortcuts import render


def main(request):
    cameras = getTableData("photos_camera")
    film = getTableData("photos_film")
    event = getTableData("photos_event")
    photos = getTableData("photos_photos")
    return render(request, "photos/index.html", {"cameras": cameras, "film": film, "event": event, "photos": photos})

def camera(request, id):
    cameras = getTableData("photos_camera")
    film = getTableData("photos_film")
    event = getTableData("photos_event")
    photos = cameraId("photos_photos", id)
    return render(request, "photos/index.html", {"cameras": cameras, "film": film, "event": event, "photos": photos})

def film(request, id):
    cameras = getTableData("photos_camera")
    film = getTableData("photos_film")
    event = getTableData("photos_event")
    photos = filmId("photos_photos", id)
    return render(request, "photos/index.html", {"cameras": cameras, "film": film, "event": event, "photos": photos})
def event(request, id):
    cameras = getTableData("photos_camera")
    film = getTableData("photos_film")
    event = getTableData("photos_event")
    photos = eventId("photos_photos", id)
    return render(request, "photos/index.html", {"cameras": cameras, "film": film, "event": event, "photos": photos})


def option(request):

    cameras = getTableData("photos_camera")
    film = getTableData("photos_film")
    event = getTableData("photos_event")
    photos = getTableData("photos_photos")
    return render(request, "photos/index.html", {"cameras": cameras, "film": film, "event": event, "photos": photos})
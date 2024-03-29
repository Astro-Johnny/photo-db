import os
from pathlib import Path

from django.db.models import Q
from django.http import HttpResponse

import settings
from photos.models import Photos, Camera, Film, Event


def getValues(allSelectParams):
    query_objects = Q()
    order_objects = []

    if 'camera' in allSelectParams:
        camera_objects = Q()
        for item in allSelectParams['camera']:
            camera_objects |= Q(camera_id=item)
        query_objects &= Q(camera_objects)

    if 'event' in allSelectParams:
        event_objects = Q()
        for item in allSelectParams['event']:
            event_objects |= Q(event_id=item)
        query_objects &= Q(event_objects)

    if 'film' in allSelectParams:
        film_objects = Q()
        for item in allSelectParams['film']:
            film_objects |= Q(film_id=item)
        query_objects &= Q(film_objects)

    if 'sort' in allSelectParams:
        if "date" in allSelectParams["sort"]:
            order_objects.append("timestamp")

        if "film" in allSelectParams["sort"]:
            order_objects.append("film_id")

        if "camera" in allSelectParams["sort"]:
            order_objects.append("camera_id")

        if "atoz" in allSelectParams["sort"]:
            order_objects.append("fileName")

    result = Photos.objects.filter(query_objects).order_by(*order_objects)
    return result


def deletePhotoById(values):
    deleteId = values["delete"]
    timestamp = values["timestamp"]
    queryset = Photos.objects.get(id=deleteId)
    filepath = Path("photos/static/photos/pictures/" + timestamp + "/" + queryset.fileName)
    if filepath.is_file():
        os.remove(filepath)
    Photos.objects.get(id=deleteId).delete()


def modifyPhotoById(values):
    saveId = values["save"]
    filename = values["filename"]
    camera = int(values["camera"])
    event = values["event"]
    film = values["film"]
    timestamp = values["timestamp"]
    filmEnd = values["filmEnd"]

    if event == '' or "none":
        event = None
    else:
        event = Event.objects.get(id=int(event)).id

    if film == '' or "none":
        film = None
    else:
        film = Film.objects.get(id=int(film)).id

    if filmEnd == '':
        filmEnd = None
    else:
        filmEnd = filmEnd

    queryset = Photos.objects.get(id=saveId)
    os.rename("photos/static/photos/pictures/" + timestamp + "/" + queryset.fileName,
              "photos/static/photos/pictures/" + timestamp + "/" + filename)

    Photos.objects.filter(id=saveId).update(
        fileName=filename,
        camera=Camera.objects.get(id=camera),
        event=event,
        film=film,
        timestamp=timestamp,
        filmEnd=filmEnd
    )


def downloadPhotoById(values):
    filename = values["download"]
    timestamp = values["timestamp"]
    path = Path("pictures/" + timestamp + "/" + filename)

    file_path = os.path.join(settings.MEDIA_ROOT, path)
    with open(file_path, 'rb') as fh:
        response = HttpResponse(fh, content_type="image/jpeg")
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        return response


def addPhotoById(values):
    filename = values["filename"]
    camera = int(values["camera"])
    event = values["event"]
    film = values["film"]
    timestamp = values["timestamp"]
    filmEnd = values["filmEnd"]

    if event == "none":
        event = None
    else:
        event = Event.objects.get(id=int(event))

    if film == "none":
        film = None
    else:
        film = Film.objects.get(id=int(film))

    if filmEnd == '':
        filmEnd = None
    else:
        filmEnd = filmEnd

    Photos.objects.create(
        fileName=filename,
        camera=Camera.objects.get(id=camera),
        event=event,
        film=film,
        timestamp=timestamp,
        filmEnd=filmEnd
    )

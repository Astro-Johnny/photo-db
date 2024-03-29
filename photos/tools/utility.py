import os
import sqlite3
from collections import namedtuple
from pathlib import Path

from django.http import HttpResponse

import settings
from photos.models import Photos, Camera, Film, Event


def namedtuplefetchall(cursor, name):
    desc = cursor.description
    nt_result = namedtuple(name, [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]


def getValues(tableName, allSelectParams):
    conditionalQuery = "WHERE"
    conditionExist = False
    sort = ""
    conditionSort = False

    if 'camera' in allSelectParams:
        if len(allSelectParams['camera']) == 1:
            conditionalQuery += f" camera_id={allSelectParams['camera'][0]}"
        else:
            conditionalQuery += f" camera_id IN {str(allSelectParams['camera'])}"
        conditionExist = True

    if 'event' in allSelectParams:
        if conditionExist:
            conditionalQuery += " AND"
        if len(allSelectParams['event']) == 1:
            conditionalQuery += f" event_id={allSelectParams['event'][0]}"
        else:
            conditionalQuery += f" event_id IN {str(allSelectParams['event'])}"
        conditionExist = True

    if 'film' in allSelectParams:
        if conditionExist:
            conditionalQuery += " AND"
        if len(allSelectParams['film']) == 1:
            conditionalQuery += f" film_id={allSelectParams['film'][0]}"
        else:
            conditionalQuery += f" film_id IN {str(allSelectParams['film'])}"
        conditionExist = True

    if not conditionExist:
        conditionalQuery = ""

    if 'sort' in allSelectParams:
        sort += "ORDER BY"
        if "date" in allSelectParams["sort"]:
            sort += " timestamp"
            conditionSort = True

        if "film" in allSelectParams["sort"]:
            if conditionSort:
                sort += ","
            sort += " film_id"
            conditionSort = True

        if "camera" in allSelectParams["sort"]:
            if conditionSort:
                sort += ","
            sort += " camera_id"
            conditionSort = True

        if "atoz" in allSelectParams["sort"]:
            if conditionSort:
                sort += ","
            sort += " fileName"

    with sqlite3.connect('./db.sqlite3') as con:
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM {tableName} {conditionalQuery} {sort}")
        result = namedtuplefetchall(cursor, f"{tableName}")
    con.close()
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

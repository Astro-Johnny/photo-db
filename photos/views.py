from photos.tools.utility import getTableData, getValues, deletePhotoById
from django.shortcuts import render


def main(request):

    if request.method == "POST":
        values = request.POST.copy()
        if "delete" in values:
            deleteId = values["delete"]
            deletePhotoById(deleteId)

    cameras = getTableData("photos_camera")
    film = getTableData("photos_film")
    event = getTableData("photos_event")
    photos = getTableData("photos_photos")
    return render(request, "photos/index.html", {"cameras": cameras, "film": film, "event": event, "photos": photos})


def option(request):
    allSelectParams = {}
    isChecked = []
    photoId = None
    sPhoto = None

    if request.method == "POST":
        values = request.POST.copy()
        if "delete" in values:
            deleteId = values["delete"]
            deletePhotoById(deleteId)
        if "save" in values:
            print(values)

    values = request.GET.copy()
    for val in values:
        [param, id] = val.split("_")

        if param in allSelectParams:
            allSelectParams[param] += (id,)
        else:
            allSelectParams[param] = (id,)
        isChecked.append(val)

    if "photo" in allSelectParams:
        photoId = int(allSelectParams["photo"][0])

    cameras = getTableData("photos_camera")
    film = getTableData("photos_film")
    event = getTableData("photos_event")
    photos = getValues("photos_photos", allSelectParams)

    if photoId:
        for photo in photos:
            if photo.id == photoId:
                sPhoto = photo

    return render(request, "photos/index.html", {"cameras": cameras, "film": film, "event": event, "photos": photos, "isChecked": isChecked, "sPhoto": sPhoto})

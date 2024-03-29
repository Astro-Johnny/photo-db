from django.core.files.storage import FileSystemStorage

from photos.tools.utility import getValues, deletePhotoById, modifyPhotoById, addPhotoById, \
    downloadPhotoById
from django.shortcuts import render, redirect
from photos.models import Photos, Camera, Film, Event

sorts = [['sort_atoz', 'A to Z'], ['sort_film', 'Film'], ['sort_date', 'Date'], ['sort_camera', 'Camera']]

def main(request):
    cameras = Camera.objects.all()
    film = Film.objects.all()
    event = Event.objects.all()
    photos = Photos.objects.all()
    for photo in photos:
        print(photo.timestamp)
    return render(request, "photos/index.html", {
        "cameras": cameras,
        "film": film,
        "event": event,
        "photos": photos,
        "sorts": sorts
    })


def option(request):
    allSelectParams = {}
    isChecked = []
    photoId = None
    sPhoto = None

    if request.method == "POST":
        values = request.POST.copy()
        if "delete" in values:
            deletePhotoById(values)
            site_url = request.build_absolute_uri()
            if "options?photo" in site_url:
                return redirect("main")
            else:
                tagList = site_url.split("&")
                tagList.pop()
                new_site_url = "&".join(tagList)
                return redirect(new_site_url)
        if "save" in values:
            modifyPhotoById(values)
        if "download" in values:
            downloadPhotoById(values)
        if "add" in values:
            addPhotoById(values)
            img = request.FILES["img"]
            filename = values["filename"]
            timestamp = values["timestamp"]
            files = FileSystemStorage(location='photos/static/photos/pictures/' + timestamp)
            files.save(filename, img)

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

    cameras = Camera.objects.all()
    film = Film.objects.all()
    event = Event.objects.all()
    photos = getValues("photos_photos", allSelectParams)

    if photoId:
        for photo in photos:
            if photo.id == photoId:
                sPhoto = photo

    return render(request, "photos/index.html",{
        "cameras": cameras,
        "film": film,
        "event": event,
        "photos": photos,
        "isChecked": isChecked,
        "sPhoto": sPhoto,
        "sorts": sorts
    })

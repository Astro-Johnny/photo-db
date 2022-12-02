from django.shortcuts import render
from photos.tools.utility import namedtuplefetchall
import sqlite3


def getTableData(tableName):
    with sqlite3.connect('./db.sqlite3') as con:
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM {tableName}")
        result = namedtuplefetchall(cursor, f"{tableName}")
    con.close()
    return result

def main(request):
    cameras = getTableData("photos_camera")
    film = getTableData("photos_film")
    event = getTableData("photos_event")
    return render(request, "photos/index.html", {"cameras": cameras, "film": film, "event": event})

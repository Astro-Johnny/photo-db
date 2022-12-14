from collections import namedtuple
import sqlite3


def namedtuplefetchall(cursor, name):
    desc = cursor.description
    nt_result = namedtuple(name, [col[0] for col in desc])
    return [nt_result(*row) for row in cursor.fetchall()]


def getTableData(tableName):
    with sqlite3.connect('./db.sqlite3') as con:
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM {tableName}")
        result = namedtuplefetchall(cursor, f"{tableName}")
    con.close()
    return result


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

def deletePhotoById(deleteId):
    with sqlite3.connect('./db.sqlite3') as con:
        cursor = con.cursor()
        #cursor.execute(f"DELETE FROM photos_photos WHERE id={deleteId};")
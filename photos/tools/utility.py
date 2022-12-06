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

def cameraId(tableName, id=None):
    with sqlite3.connect('./db.sqlite3') as con:
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM {tableName} WHERE camera_id={id}")
        result = namedtuplefetchall(cursor, f"{tableName}")
    con.close()
    return result

def filmId(tableName, id=None):
    with sqlite3.connect('./db.sqlite3') as con:
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM {tableName} WHERE film_id={id}")
        result = namedtuplefetchall(cursor, f"{tableName}")
    con.close()
    return result

def eventId(tableName, id=None):
    with sqlite3.connect('./db.sqlite3') as con:
        cursor = con.cursor()
        cursor.execute(f"SELECT * FROM {tableName} WHERE event_id={id}")
        result = namedtuplefetchall(cursor, f"{tableName}")
    con.close()
    return result

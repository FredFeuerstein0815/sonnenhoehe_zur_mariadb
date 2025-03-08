#!/usr/bin/env python3
# coding=utf-8

from astral import LocationInfo
from astral import moon
from mysql.connector import errorcode
import datetime
import mysql.connector

ort = LocationInfo(name='Freiburg', region='Germany', timezone='Europe/Berlin', latitude=48.0, longitude=7.8)
jahr=datetime.datetime.today().year
print("Jahr {}".format(jahr))
monat=datetime.datetime.today().month
print("Monat {}".format(monat))
tag=datetime.datetime.today().day
print("Tag {}".format(tag))
print("Longitude {}".format(ort.longitude))
print("Latitude {}".format(ort.latitude))
mondphase = int("{0:.0f}".format(moon.phase(datetime.date(jahr, monat, tag))))
print("Mondphase {}".format(mondphase))
try:
    mondphase=abs(mondphase)
    print("Eintrag Datenbank {}".format(mondphase))
    db = mysql.connector.connect(user='mondphase', password='mondphase', host='127.0.0.1', database='mondphase')
    cursor = db.cursor(prepared=True)
    sql = "INSERT INTO daten (mondphase) VALUES (%s)"
    val = (mondphase,)
    cursor.execute(sql,val)
    db.commit()
    cursor.close()
    db.close()
except Exception as error:
    print(error)

#!/usr/bin/env python3
# coding=utf-8

from astral import LocationInfo
from astral import moon
from astral import sun
import datetime
from mysql.connector import errorcode
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
sonnenazimuth = int("{0:.0f}".format(sun.azimuth(ort.observer)))
sonnenzenith = int("{0:.0f}".format(sun.zenith(ort.observer)))
print("Azimut der Sonne {}".format(sonnenazimuth))
print("Zenit der Sonne {}".format(sonnenzenith))
sonnenhoehe = (sonnenzenith-90)
if sonnenhoehe < 0:
    print("Sonne über dem Horizont: {}°".format(abs(sonnenhoehe)))
    try:
        sonnenhoehe=abs(sonnenhoehe)
        print("Eintrag Datenbank {}".format(sonnenhoehe))
        db = mysql.connector.connect(user='sonne', password='sonne', host='127.0.0.1', database='sonne')
        cursor = db.cursor(prepared=True)
        sql = "INSERT INTO daten (sonnenhoehe, sonnenazimuth) VALUES (%s, %s)"
        val = (sonnenhoehe, sonnenazimuth)
        cursor.execute(sql,val)
        db.commit()
        cursor.close()
        db.close()
    except Exception as error:
        print(error)
else:
    print(sonnenhoehe)
mondazimuth = ("{0:.0f}".format(moon.azimuth(ort.observer)))
print("Azimut des Mondes {}".format(mondazimuth))
mondzenith = int("{0:.0f}".format(moon.zenith(ort.observer)))
print("Zenit des Mondes {}".format(mondzenith))
mondhoehe = (mondzenith-90)
#print(mondhoehe)
if mondhoehe < 0:
    print("Mond über dem Horizont: {}°".format(abs(mondhoehe)))
    try:
        mondhoehe=abs(mondhoehe)
        print("Eintrag Datenbank {}".format(mondhoehe))
        db = mysql.connector.connect(user='mond', password='mond', host='127.0.0.1', database='mond')
        cursor = db.cursor(prepared=True)
        sql = "INSERT INTO daten (mondhoehe, mondazimuth) VALUES (%s, %s)"
        val = (mondhoehe, mondazimuth)
        cursor.execute(sql,val)
        db.commit()
        cursor.close()
        db.close()
    except Exception as error:
        print(error)

else:
    print(mondhoehe)

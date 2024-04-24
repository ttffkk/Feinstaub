import csv
import os
import mysql.connector
from CSV_Download import CSV_Downloader

config = {
    'user': 'root',
    'password': 'DkEab99729777',
    'host': '127.0.0.1',  # Remove the port number from the host
    'database': 'feinstaub',
    'raise_on_warnings': True
}
print("Willkommen zu unseren Feinstaub Projekt!")
print("Folgende Daten können aufgerufen werden:")
print("1.Temperatur")
print("2.Luftfeuchtigkeit")
print("3.Feinstaubmessungen")
userInput = int(input())

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

def getDataTemp():
    print("Cool, du willst also Daten für die Temperatur haben!")
    print("Die Daten basieren auf das Jahr 2022 von Januar bis Mai")
    print("Bitte gib ein Datum in folgenden Format an: MM-TT")
    datetime = "2022-" + input() + "%"
    min_query = "select MIN(temperatur) from feinstaub.dht22 where zeitstempel like %s"
    max_query = "select MAX(temperatur) from feinstaub.dht22 where zeitstempel like %s"
    avg_query = "select AVG(temperatur) from feinstaub.dht22 where zeitstempel like %s"

    cursor.execute(min_query, (datetime,))
    min_temperatur = round(cursor.fetchone()[0], 2)
    print("Mindesttemperatur:", min_temperatur, "°C")

    cursor.execute(max_query, (datetime,))
    max_temperatur = round(cursor.fetchone()[0], 2)
    print("Maxmimaltemperatur:", max_temperatur, "°C")

    cursor.execute(avg_query, (datetime,))
    avg_temperatur = round(cursor.fetchone()[0], 2)
    print("Durchschnittstemperatur:", avg_temperatur, "°C")

    cursor.close()
    cnx.close()


def getDataHumidity():
    print("Hello World")

def getDataParticles():
    print("asd")

if 0 < userInput < 4:
    if userInput == 1:
        getDataTemp()
    elif userInput == 2:
        getDataHumidity()
    elif userInput == 3:
        getDataParticles()

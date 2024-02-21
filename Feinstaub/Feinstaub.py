import sqlite3

# Funktion, um Daten in die Tabelle einzufügen
def insertDataIntoTable():
    conn = sqlite3.connect('Feinstaub.sql')
    cursor = conn.cursor()
    cursor.execute("insert into SDS011 (PM10, PM25, zeitstempel) values (?, ?, ?)")
    cursor.execute("insert into DHT22 (luftfeuchtigkeit, zeitstempel, temperatur) values (?, ?, ?)")
    # csv Daten mit müssen noch gesettet werden
    conn.close()

# Funktion, um Daten aus der Tabelle heraus zu bekommen
def getDataFromTable():
    conn = sqlite3.connect('Feinstaub.sql')
    cursor = conn.cursor()
    cursor.execute("select * from SDS011 where zeitstempel like 2022-03-14")
    ergebnisse = cursor.fetchall()
    for row in ergebnisse:
        print(row)
    conn.close()
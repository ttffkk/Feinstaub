import mysql.connector

config = {
    'user': 'root',
    'password': 'Arian2001',
    'host': '127.0.0.1:3306',
    'database': 'employees',
    'raise_on_warnings': True #hier müssen die daten noch angepasst werden
}
cnx = mysql.connector.connect(**config)


# Funktion, um Daten in die Tabelle einzufügen
def insertDataIntoTable():
    cursor = cnx.cursor()
    cursor.execute("insert into SDS011 (PM10, PM25, zeitstempel) values (?, ?, ?)")
    cursor.execute("insert into DHT22 (luftfeuchtigkeit, zeitstempel, temperatur) values (?, ?, ?)")
    # csv Daten mit müssen noch gesettet werden
    cnx.close()

# Funktion, um Daten aus der Tabelle heraus zu bekommen
def getDataFromTable():
    cursor = cnx.cursor()
    cursor.execute("select * from SDS011 where zeitstempel like 2022-03-14")
    ergebnisse = cursor.fetchall()
    for row in ergebnisse:
        print(row)
    cnx.close()

import csv
import mysql.connector

config = {
    'user': 'root',
    'password': 'Arian2001',
    'host': '127.0.0.1',  # Remove the port number from the host
    'database': 'feinstaub',
    'raise_on_warnings': True
}

# Establish a connection to the database
cnx = mysql.connector.connect(**config)


# Function to insert data into the table
def insertDataIntoTableSds011(data):
    cursor = cnx.cursor()
    cursor.execute("INSERT INTO feinstaub.sds011 (PM10, PM25, zeitstempel) VALUES (%s, %s, %s)", data)



def insertDataIntoTableDht22(data):
    cursor = cnx.cursor()
    cursor.execute("INSERT INTO feinstaub.dht22 (luftfeuchtigkeit, zeitstempel, temperatur) VALUES (%s, %s, %s)", data)



# Open the CSV file and read the data
with open('../CSV_Download/csvSds011/2022-01-01.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=';')
    next(csv_reader)  # Skip the header row if it exists
    for row in csv_reader:

        sensor_id, sensor_type, location, lat, lon, timestamp, P1, durP1, ratioP1, P2, durP2, ratioP2 = row
        data = (P1, P2, timestamp)
        insertDataIntoTableSds011(data)

with open('../CSV_Download/csvDht22/2022-01-01.csv', 'r') as csvfile:
    csv_reader2 = csv.reader(csvfile, delimiter=';')
    next(csv_reader2)  # Skip the header row if it exists
    for row2 in csv_reader2:

        sensor_id, sensor_type, location, lat, lon, timestamp, temperature, humidity = row2
        data = (humidity, timestamp, temperature)
        insertDataIntoTableDht22(data)

cnx.commit()  # Commit the transaction
cnx.close()

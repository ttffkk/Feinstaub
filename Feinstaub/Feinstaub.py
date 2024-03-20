import csv
import os
import mysql.connector
from CSV_Download import CSV_Downloader

config = {
    'user': 'root',
    'password': 'RootPassword',
    'host': '127.0.0.1',  # Remove the port number from the host
    'database': 'feinstaub',
    'raise_on_warnings': True
}

# Establish a connection to the database
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()


# Function to insert data into the table
def insertDataIntoTableSds011(data):
    cursor.execute("INSERT INTO feinstaub.sds011 (PM10, PM25, zeitstempel) VALUES (%s, %s, %s)", data)


def insertDataIntoTableDht22(data):
    cursor.execute("INSERT INTO feinstaub.dht22 (luftfeuchtigkeit, zeitstempel, temperatur) VALUES (%s, %s, %s)", data)


# Open the CSV file and read the data

def fileToTable(file, type_of_table):
    with open(file, 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=';')
        next(csv_reader)  # Skip the header row if it exists
        for row in csv_reader:

            # Assuming the CSV columns are in the order PM10, PM25, and zeitstempel
            sensor_id, sensor_type, location, lat, lon, timestamp, P1, durP1, ratioP1, P2, durP2, ratioP2 = row
            data = (P1, P2, timestamp)
            if type_of_table == "DHT22":
                insertDataIntoTableDht22(data)
            elif type_of_table == "SDS011":
                insertDataIntoTableSds011(data)
            else:
                print("Unknown")


def fileCatcher():
    type_of_table = "sds011"
    sensor_id_outside = 3659
    csv_folder_sds = f"{CSV_Downloader.download_files(type_of_table, sensor_id_outside)}"
    type_of_table = "dht22"
    sensor_id_outside = 3660
    csv_folder_dht = f"{CSV_Downloader.download_files(type_of_table, sensor_id_outside)}"

    for filename in os.listdir(csv_folder_sds):
        if filename.endswith('.csv'):
            full_path = os.path.join(csv_folder_sds, filename)
            fileToTable(full_path, "SDS011")
    for filename in os.listdir(csv_folder_dht):
        if filename.endswith('.csv'):
            full_path = os.path.join(csv_folder_dht, filename)
            fileToTable(full_path, "DHT22")


fileCatcher()
cnx.commit()  # Commit the transaction
cnx.close()

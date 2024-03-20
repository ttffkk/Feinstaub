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

# Establish a connection to the database
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()


# Function to insert data into the table
def insert_data_into_table_sds011(data):
    cursor.execute("INSERT INTO feinstaub.sds011 (PM10, PM25, zeitstempel) VALUES (%s, %s, %s)", data)


def insert_data_into_table_dht22(data):
    cursor.execute("INSERT INTO feinstaub.dht22 (luftfeuchtigkeit, zeitstempel, temperatur) VALUES (%s, %s, %s)", data)


# Open the CSV file and read the data

def file_to_table(file, type_of_table):
    with open(file, 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=';')
        next(csv_reader)  # Skip the header row if it exists
        for row in csv_reader:

            # Assuming the CSV columns are in the order PM10, PM25, and zeitstempel
            if type_of_table == "DHT22":
                sensor_id, sensor_type, location, lat, lon, timestamp, temperature, humidity = row
                data = (humidity, timestamp, temperature)
                insert_data_into_table_dht22(data)
            elif type_of_table == "SDS011":
                sensor_id, sensor_type, location, lat, lon, timestamp, p1, dur_p1, ratio_p1, p2, dur_p2, ratio_p2 = row
                data = (p1, p2, timestamp)
                insert_data_into_table_sds011(data)
            else:
                print("Unknown")


def file_catcher():
    type_of_table = "sds011"
    sensor_id_outside = 3659
    csv_folder_sds = f"{CSV_Downloader.download_files(type_of_table, sensor_id_outside)}"
    type_of_table = "dht22"
    sensor_id_outside = 3660
    csv_folder_dht = f"{CSV_Downloader.download_files(type_of_table, sensor_id_outside)}"

    for filename in os.listdir(csv_folder_sds):
        if filename.endswith('.csv'):
            full_path = os.path.join(csv_folder_sds, filename)
            file_to_table(full_path, "SDS011")
    for filename in os.listdir(csv_folder_dht):
        if filename.endswith('.csv'):
            full_path = os.path.join(csv_folder_dht, filename)
            file_to_table(full_path, "DHT22")


file_catcher()
cnx.commit()  # Commit the transaction

cnx.close()

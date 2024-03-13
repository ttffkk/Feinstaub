import csv
import os
import mysql.connector

config = {
    'user': 'root',
    'password': 'DkEab99729777',
    'host': '127.0.0.1',  # Remove the port number from the host
    'database': 'feinstaub',
    'raise_on_warnings': True
}

# Establish a connection to the database
cnx = mysql.connector.connect(**config)

# Function to insert data into the table
def insertDataIntoTable(data):
    cursor = cnx.cursor()
    cursor.execute("INSERT INTO SDS011 (PM10, PM25, zeitstempel) VALUES (%s, %s, %s)", data)



def fileCatcher():
    csv_folder = '../CSV_Download/csv'
    for filename in os.listdir(csv_folder):
        if filename.endswith('.csv'):
            full_path = os.path.join(csv_folder, filename)
            fileToTable(full_path)


# Open the CSV file and read the data
def fileToTable(file):
    with open(file, 'r') as csvfile:
        csv_reader = csv.reader(csvfile, delimiter=';')
        next(csv_reader)  # Skip the header row if it exists
        for row in csv_reader:

            # Assuming the CSV columns are in the order PM10, PM25, and zeitstempel
            sensor_id, sensor_type, location, lat, lon, timestamp, P1, durP1, ratioP1, P2, durP2, ratioP2 = row
            data = (P1, P2, timestamp)
            insertDataIntoTable(data)

    # Close the database connection


fileCatcher()
cnx.commit()
cnx.close()

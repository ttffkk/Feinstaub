import datetime
import gzip
import os
import shutil
import urllib
import urllib.request
from urllib.error import HTTPError


def download(url):
    """
    Download and return data from the given URL.
    """
    try:
        response = urllib.request.urlopen(url)
        datas = response.read()
        return datas
    except HTTPError as e:
        print(f'HTTP Error from {url} : {e}')


def save(data, filename):
    """Save data into the given filename."""
    if filename.endswith(".gz"):
        with open(filename, 'wb') as f:
            f.write(data)
    else:
        with open(filename, 'wt') as f:
            f.write(data)


def get_dates_2022():
    dates_2022 = []
    current_date = datetime.date(2022, 1, 1)
    while current_date.year == 2022:
        dates_2022.append(current_date.strftime("%Y-%m-%d"))
        current_date += datetime.timedelta(days=1)
    return dates_2022

def extract(gz_file, extracted_file):
    with gzip.open(gz_file, 'rb') as f_in:
        with open(extracted_file, 'wb') as f_out:
            shutil.copyfileobj(f_in, f_out)


def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f'Folder {directory} added')
    else:
        print(f'Folder {directory} already exists')


create_directory("csv")
create_directory("gz")
filepath = "csv"
dates_2022 = get_dates_2022()
for date in dates_2022:
    url = f"https://archive.sensor.community/2022/{date}/{date}_sds011_sensor_3659.csv.gz"
    filepath = f"gz/{date}.csv.gz"
    newFilepath = f"csv/{date}.csv"
    print(f"Downloading from", url)
    data = download(url)
    if data:
        save(data, filepath)
        extract(filepath, newFilepath)
        print(f"Extracting", newFilepath)
    else:
        print(f"No data")

if os.path.exists("gz"):
    shutil.rmtree("gz")

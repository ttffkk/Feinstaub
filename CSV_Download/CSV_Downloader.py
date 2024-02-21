import urllib

import requests
import datetime
import os


def download(url):
    """
    Download and return data from the given URL.
    """
    data = urllib.request.urlopen(url).read()
    return data

def save(data, filename):
    'Save data into the given filename.'
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


filepath = "csv"
dates_2022 = get_dates_2022()
for date in dates_2022:
    url = f"https://archive.sensor.community/2022/{date}/{date}_sds011_sensor_3659.csv.gz"
    filepath = f"gz/{date}.csv.gz"
    print(f"Downloading from",url)
    data = download(url)
    save(data, filepath)

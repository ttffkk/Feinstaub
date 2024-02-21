import urllib.request
import datetime


def download(url):
    """
    Download and return data from the given URL.
    """
    data = urllib.request.urlopen(url).read()
    return data


def save(data, filename):
    """Save data into the given filename."""
    with open(filename, 'wt') as f:
        f.write(data)


def get_dates_2022():
    dates_2022 = []
    current_date = datetime.date(2022, 1, 1)
    while current_date.year == 2022:
        dates_2022.append(current_date.strftime("%Y-%m-%d"))
        current_date += datetime.timedelta(days=1)
    return dates_2022

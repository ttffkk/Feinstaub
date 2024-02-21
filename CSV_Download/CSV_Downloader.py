import urllib.request
import datetime

def download(url):
    """
    Download and return data from the given URL.
    """
    data = urllib.request.urlopen(url).read()
    return data

def save(data, filename):
    'Save data into the given filename.'
    with open(filename, 'wt') as f:
        f.write(data)


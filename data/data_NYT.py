import csv
import io
import requests

url = "https://raw.githubusercontent.com/nytimes/covid-19-data/master/live/us-counties.csv"


def get_nyt_data(url):
    r = requests.get(url)
    buff = io.StringIO(r.text)
    dr = csv.DictReader(buff)
    return dr


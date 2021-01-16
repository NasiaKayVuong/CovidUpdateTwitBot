import daily_average as da
import data_NYT as ny
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import datetime


def format_data(data):
    nyt_list = [{"county_state": row["county"] + ", " + row["state"], "cases": row["cases"]} for row in list(data)]
    return {"data": nyt_list}


def upload_data(data):
    db = firestore.client()
    db.collection("daily_data").document(str(datetime.date.today())).set(format_data(data))


cred = credentials.Certificate("../../creds/coviddailytwitterbot-firebase-adminsdk-dwcre-27e5f3b48a.json")
firebase_admin.initialize_app(cred, {
  'projectId': "coviddailytwitterbot",
})

nyt_data = ny.get_nyt_data("https://raw.githubusercontent.com/nytimes/covid-19-data/master/live/us-counties.csv")
daily_avg = da.get_daily_avg("https://covid.cdc.gov/covid-data-tracker/COVIDData/getAjaxData?id=US_MAP_DATA")



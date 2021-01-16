import requests
import json

url = "https://covid.cdc.gov/covid-data-tracker/COVIDData/getAjaxData?id=US_MAP_DATA"
def get_daily_avg(link):
    response = requests.get(link)
    cdc_data = json.loads(response.text)
    daily_avg = cdc_data["US_MAP_DATA"][-1]["Seven_day_avg_new_cases_per_100k"]
    return daily_avg

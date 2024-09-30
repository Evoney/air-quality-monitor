import requests
from config import Config

metric = Config.AIR_METRIC

def collect_data():
    params = {"api_key": Config.API_KEY}
    fields = f'?fields=sensor_index,latitude,longitude,{metric},last_seen'
    response = requests.get(Config.API_URL + Config.SENSOR_ID + fields, params=params)
    return response.json()['sensor']
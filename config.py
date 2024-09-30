class Config:
    CSV_FILE = "historical_air_quality_data.csv"
    API_KEY = ""
    SENSOR_ID = ""
    AIR_METRIC = "pm2.5_atm"
    API_URL = "https://api.purpleair.com/v1/sensors/"
    SPARK_APP_NAME = "AirQualityMonitor"
    HADOOP_DATA_PATH = "hdfs://localhost:9000/user/hadoop/air_quality_data"
    UPDATE_INTERVAL = 5  # Time in seconds to update the data
    MAP_CENTER = [-3.096909, -59.969593] # Latitude/longitude
    MAP_ZOOM_START = 13 # Zoom parameter
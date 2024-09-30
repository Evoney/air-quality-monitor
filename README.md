# Clean Air - Real-Time Air Quality Monitoring

## About the Project

Clean Air is a real-time air quality monitoring application designed to provide accurate and up-to-date information about air quality in various urban areas. This tool aims to help citizens make informed decisions about their outdoor activities, promoting a healthier lifestyle and environmental awareness.

## Main Features

- Real-time data collection through air quality APIs
- Processing and analysis of large volumes of data using PySpark
- Historical data storage in Hadoop
- Statistical analysis and identification of seasonal patterns
- Interactive data visualization through charts and maps
- Periodic automatic updates

## Requirements

- Python 3.8+
- PurpleAir API (https://api.purpleair.com/)
- Apache Spark 3.5.2 (https://spark.apache.org/downloads.html)
- Apache Hadoop (for historical data storage)
- Dependencies listed in the `requirements.txt` file

## Installation

1. Install dependencies:

```
pip install -r requirements.txt
```

2. Configure the Hadoop and Spark environment as necessary.

3. Replace the API key in the `config.py` file.

## Usage

Run the main script:

```
python main.py
```

## Acknowledgments

- PurpleAir API: Primary source of air quality data
- Apache Spark and Hadoop: Big Data processing and storage technologies
- Matplotlib and Folium: Data visualization libraries

## Roadmap

- Improve integration with multiple data sources
- Implement an interactive web dashboard
- Add alert features based on specific conditions
- Expand analysis to include air quality predictions

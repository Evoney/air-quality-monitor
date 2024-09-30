import os
from pyspark.sql import SparkSession
import pandas as pd
import time
from datetime import datetime
from config import Config
from data_collector import collect_data
from data_processor import process_data, create_csv_file, update_csv_file
from data_analyzer import analyze_data
from view import visualize_data

# Configuração do ambiente
os.environ['PYSPARK_SUBMIT_ARGS'] = '--packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.2 pyspark-shell'

# Inicialização do Spark
spark = SparkSession.builder.master("local").config('spark.sql.debug.maxToStringFields', 2000).appName(Config.SPARK_APP_NAME).getOrCreate()

def save_to_hadoop(df):
    spark_df = spark.createDataFrame(df)
    spark_df.write.parquet(Config.HADOOP_DATA_PATH, mode="append")

def main():
    # Coleta inicial de dados
    raw_data = collect_data()
    
    # Processa os dados da primeira coleta
    processed_data = process_data(raw_data)
    
    # Cria o arquivo CSV na primeira coleta
    create_csv_file(processed_data)
    
    # Análise inicial
    analyze_data(processed_data)
    
    # Visualização inicial
    visualize_data(processed_data)
    
    # Salva dados históricos no Hadoop
    # save_to_hadoop(processed_data)
    
    print(f"Dados coletados em {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    while True:
        # Coleta de dados
        raw_data = collect_data()
        
        # Processamento de dados
        processed_data = process_data(raw_data)

        # Atualização do arquivo CSV com os novos dados
        update_csv_file(processed_data)

        # Atualização da análise com os novos dados
        df = pd.read_csv(Config.CSV_FILE)
        df['last_seen'] = pd.to_datetime(df['last_seen'], format='%Y-%m-%d  %H:%M:%S')
        analyze_data(df)
        
        # Atualização da visualização com os novos dados
        visualize_data(df)
        
        # Salva dados históricos no Hadoop
        # save_to_hadoop(pd.read_csv(Config.CSV_FILE))
        
        # Aguardar por alguns minutos antes da próxima coleta
        print(f"Dados atualizados em {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        time.sleep(Config.UPDATE_INTERVAL)

if __name__ == "__main__":
    main()

import os
import pandas as pd
from config import Config

metric = Config.AIR_METRIC

def categorize_air_quality(pm25_value):
    """
    Classifica a qualidade do ar com base no valor de PM2.5.
    """
    if pm25_value <= 12.0:
        return "Bom"
    elif pm25_value <= 35.0:
        return "Moderado"
    elif pm25_value <= 55.0:
        return "Insalubre"
    elif pm25_value <= 150.0:
        return "Insalubre para grupos sensíveis"
    else:
        return "Perigoso"

def process_data(raw_data):
    df = pd.DataFrame.from_dict([raw_data])
    df['last_seen'] = pd.to_datetime(df['last_seen'], unit='s')
    df[metric] = df[metric].astype(float)

    # Adiciona uma nova coluna para classificar a qualidade do ar
    df['quality_category'] = df[metric].apply(categorize_air_quality)

    return df

def create_csv_file(df):
    """
    Cria um novo arquivo CSV com os dados de last_seen e pm2_5_atm.
    """
    # Cria o arquivo CSV na primeira coleta
    if os.path.exists(Config.CSV_FILE):
        os.remove(Config.CSV_FILE)
    
    df.to_csv(Config.CSV_FILE, index=False, mode='w')

def update_csv_file(df):
    """
    Atualiza o arquivo CSV existente com novos dados de last_seen e pm2_5_atm.
    """
    # Lê o arquivo CSV existente
    if os.path.exists(Config.CSV_FILE):
        existing_df = pd.read_csv(Config.CSV_FILE)
        
        # Concatena os novos dados ao existente
        updated_df = pd.concat([existing_df, df])
        
        # Salva os dados atualizados
        updated_df.to_csv(Config.CSV_FILE, index=False, mode='w')
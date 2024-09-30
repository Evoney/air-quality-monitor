import pandas as pd
from config import Config

def analyze_data(df):
    metric = Config.AIR_METRIC
    stats = df[metric].describe()
    print("Estatísticas da qualidade do ar:")
    print(stats)
    
    df['month'] = df['last_seen'].dt.month
    seasonal_patterns = df.groupby('month')[metric].mean().sort_values(ascending=False)
    print("\nPadrões sazonais na poluição do ar:")
    print(seasonal_patterns)

    # Adiciona análise da categoria de qualidade do ar
    category_counts = df['quality_category'].value_counts()
    print("\nDistribuição das categorias de qualidade do ar:")
    print(category_counts)
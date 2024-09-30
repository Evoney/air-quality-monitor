import matplotlib.pyplot as plt
import folium
from config import Config

def visualize_data(df):
    metric = Config.AIR_METRIC

    # Extrai os dados necessários
    timestamps = df['last_seen']
    metric_data = df[metric]

    # Cria um subplot com duas linhas
    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(15, 10))

    # Plot do PM2.5 ao longo do tempo
    ax1.plot(timestamps, metric_data, marker='o')
    ax1.set_title('PM2.5 ao Longo do Tempo')
    ax1.set_xlabel('Data/Hora')
    ax1.set_ylabel('PM2.5 (μg/m³)')
    ax1.grid(True)

    # Adiciona uma linha média móvel
    window_size = 7
    rolling_mean = df[metric].rolling(window=window_size).mean()
    ax1.plot(timestamps[window_size-1:], rolling_mean[window_size-1:], label='Média Móvel de 7 Dias', color='orange')

    # Legendas
    ax1.legend()

    # Plot da qualidade do ar ao longo do tempo
    ax2.plot(timestamps, df['quality_category'])
    ax2.set_title('Qualidade do Ar ao Longo do Tempo')
    ax2.set_xlabel('Data/Hora')
    ax2.set_ylabel('Categoria de Qualidade do Ar')
    ax2.grid(True)

    # Adiciona uma legenda para as categorias de qualidade do ar
    categories = ['Bom', 'Moderado', 'Insalubre', 'Insalubre para grupos sensíveis', 'Perigoso']
    colors = ['green', 'yellow', 'orange', 'red', 'purple']
    for i, category in enumerate(categories):
        ax2.axhspan(i-0.25, i+0.25, color=colors[i], alpha=0.2, label=category)

    # Legendas
    ax2.legend()

    # Configura o layout dos subplots
    plt.tight_layout()
    plt.subplots_adjust(hspace=0.3)

    # Salva os gráficos
    plt.savefig('air_quality_plot.png')
    plt.close(fig)

    map = folium.Map(location=Config.MAP_CENTER, zoom_start=Config.MAP_ZOOM_START)
    colors = {
        "Bom": 'green',
        "Moderado": 'yellow',
        "Insalubre": 'orange',
        "Insalubre para grupos sensíveis": 'red',
        "Perigoso": 'purple'
    }
    
    for _, row in df.iterrows():
        folium.Marker([row['latitude'], row['longitude']], 
                      popup=f"PM2.5: {row[metric]} μg/m³\nCategoria: {row['quality_category']}",
                      icon=folium.Icon(color=colors[row['quality_category']])).add_to(map)
    map.save('air_quality_map.html')
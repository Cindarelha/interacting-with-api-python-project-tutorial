import os
import pandas as pd
import seaborn as sns
from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import matplotlib.pyplot as plt

# Cargar las variables de entorno del archivo .env
load_dotenv()

# Obtener las credenciales de Spotify de las variables de entorno
client_id = os.getenv('SPOTIPY_CLIENT_ID')
client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')

# Verificar que las variables de entorno se cargaron correctamente
if not client_id or not client_secret:
    raise Exception("No se encontraron las credenciales de Spotify en las variables de entorno")

# Inicializar el cliente de Spotify con las credenciales obtenidas
spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

birdy_uri = 'spotify:artist:3jNkaOXasoc7RsxdchvEVq' # Chase & Status

# Obtener todos los álbumes del artista


# Obtener las pistas principales del artista
try:
    results = spotify.artist_top_tracks(birdy_uri)
    tracks_data = []
    for track in results['tracks'][:10]:
            track_info = {
                'name': track['name'],
                'popularity': track['popularity'],
                'duration_ms': track['duration_ms']
            }
            tracks_data.append(track_info)
            

            
    # Convertir a DataFrame
    df = pd.DataFrame(tracks_data)
        
    # Ordenar por popularidad de manera creciente
    df_sorted = df.sort_values(by='popularity', ascending=False)
    
    # Mostrar el top 3 resultante
    top_3_tracks = df_sorted.head(3)
    print(df.columns)
    
    # Crear un scatter plot para analizar la relación entre duración y popularidad
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=df, x='duration_ms', y='popularity')
    plt.title('Relación entre Duración de Canciones y Popularidad')
    plt.xlabel('Duración (ms)')
    plt.ylabel('Popularidad')
    plt.show()
     # Guardo porque no me abre ventana emergente
    plt.savefig('relacion_duracion_popularidad.png')

    #ANALISIS RESULTADOS GRAFICOS:
        # puntos dispersos sin un patrón claro 
        # No hay una relación significativa entre la duración de las canciones y su popularidad.
except Exception as e:
    print(f"Error al obtener las pistas principales: {e}")
finally:
# Liberar recursos 
    spotify = None
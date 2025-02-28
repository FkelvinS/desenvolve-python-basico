import csv
import pandas as pd

# Passo 1: Carregar o arquivo CSV
file_path = 'spotify-2023.csv'

# Carregar o arquivo com encoding='latin-1'
with open(file_path, mode='r', encoding='latin-1') as file:
    # Criar um objeto csv.reader para ler o conteúdo do arquivo
    csv_reader = csv.reader(file)
    
    # Ignorar a primeira linha (cabeçalho)
    header = next(csv_reader)
    
    # Passo 2: Filtrar as linhas válidas (músicas no intervalo de 2012 a 2022)
    valid_rows = []
    
    for row in csv_reader:
        if len(row) == 10:  # Garantir que a linha tem 10 colunas
            track_name, artist_name, artist_count, released_year, released_month, released_day, \
            in_spotify_playlists, in_spotify_charts, streams, in_apple_playlists = row

            # Ignorar linhas com aspas extras (caso o artista tenha mais de um nome)
            if '"' in track_name or '"' in artist_name:
                continue  # Ignorar músicas com formato inválido

            # Filtrar somente músicas de 2012 a 2022
            try:
                released_year = int(released_year)
                streams = int(streams)
                if 2012 <= released_year <= 2022:
                    valid_rows.append([track_name, artist_name, released_year, streams])
            except ValueError:
                continue  # Ignorar qualquer linha que tenha erro de conversão para número

# Passo 3: Criar um DataFrame com o Pandas
df = pd.DataFrame(valid_rows, columns=["track_name", "artist_name", "released_year", "streams"])

# Passo 4: Encontrar a música mais tocada de cada ano entre 2012 e 2022
top_tracks = []

for year in range(2012, 2023):
    # Filtrar músicas do ano específico
    year_data = df[df['released_year'] == year]
    
    # Verificar se o DataFrame para o ano não está vazio
    if not year_data.empty:
        # Encontrar a música com o maior número de streams
        top_track = year_data.loc[year_data['streams'].idxmax()]
        
        # Adicionar à lista com as informações desejadas
        top_tracks.append([top_track["track_name"], top_track["artist_name"], top_track["released_year"], top_track["streams"]])

# Passo 5: Imprimir a lista de músicas mais tocadas de cada ano
print(top_tracks)


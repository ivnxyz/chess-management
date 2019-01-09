import csv
import random
import json

# Este módulo maneja los datos de jugadores.
# Contiene métodos para agregar y obtener datos de jugadores.

# Esta función importa la lista de jugadores
def import_players():
    try: 
        with open('players_data.csv', 'r') as players_file:
            # Crear lector csv
            reader = csv.reader(players_file)

            # Lista de jugadores
            players = []

            # Iterar por las filas
            for index, row in enumerate(reader):
                # Ignorar la primera fila (header)
                if index == 0:
                    continue
                else:
                    # Eliminar espacios en blanco y mejorar formato
                    name = row[1].strip(' ').title()
                    players.append(name)

            # Regresar lista de jugadores
            return players
    except:
        print("Falta el archivo players_data.csv") 
        return []

# Esta función guarda los datos de los jugadores importados
def save_players_data(players):
    # Desordenar lista de jugadores
    random.shuffle(players)

    # Generar archivo
    with open('chess.json', 'w') as chess_file:
        # Generar diccionario vacío
        data = {}

        # Iterar por la lista de jugadores
        for index, player in enumerate(players):
            # Generar llave
            key = index + 1
            data[key] = player

            print(player, '-', key)

        # Guardar datos
        json.dump({ 'players': data }, chess_file, ensure_ascii=False)

# Obtener los datos de un jugador del archivo json
def get_player_data(player_id):
    try:
        # Abrir archivo JSON
        with open('chess.json') as chess_file:
            # Obtener datos
            data = json.load(chess_file)
            
            try:
                # Obtener jugadores
                players = data['players']
                try:
                    # Obtener y regresar jugador
                    player = players[str(player_id)]
                    return player
                # En caso de que no exista el jugador
                except KeyError:
                    print('No existe ese jugador')
            except KeyError:
                # Imprimir error
                print('No hay datos de jugadores')
    except IOError:
        # Imprimir error
        print('Aún no hay archivos de jugadores')

    # Regresar None
    return None

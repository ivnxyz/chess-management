import json
import random
from players import *

# Este módulo maneja todas las partidas.
# Contiene métodos para agregar y obtener datos de partidas.

# Colores
COLORS = ['Blancas', 'Negras']

# Abrir archivo de ajedrez
def get_chess_file_data():
    with open('chess.json') as chess_file:
        data = json.load(chess_file)
        return data

# Empezar una nueva partida usando el id de cada usuario
def start_new_match(player_one_id, player_two_id, game_id):
    # Obtener jugadores
    player_one = 'Iván Martínez' # TODO: Obtener jugador
    player_two = 'Alejandro Pineda' # TODO: Obtener jugador

    # Asignar colores de manera aleatoria
    player_one_color = random.choice(COLORS)
    player_two_color = ''

    # Asignar color del segundo jugador
    if player_one_color == COLORS[0]:
        player_two_color = COLORS[1]
    else:
        player_two_color = COLORS[0]

    # Crear datos que serán guardados
    game_data = {
        'player_one': {
            'name': player_one,
            'color': player_one_color
        },
        'player_two': {
            'name': player_two,
            'color': player_two_color
        },
        'winner': ' - '
    }

    # Obtener datos
    chess_file_data = get_chess_file_data()

    try:
        # Asegurarse de que no hay un juego con el mismo id
        try:
            game = chess_file_data["games"][str(game_id)]
            print('Ya hay datos de ese juego')
        # En caso de que no haya, guardamos nuevos datos
        except KeyError:
            chess_file_data["games"][str(game_id)] = game_data
            # Imprimir datos
            print(player_one, '-', player_one_color)
            print(player_two, '-', player_two_color)
    except KeyError:
        # Crear lista "games"
        chess_file_data["games"] = {
            str(game_id): game_data
        }
        # Imprimir datos
        print(player_one, '-', player_one_color)
        print(player_two, '-', player_two_color)

    # Guardar datos
    save_chess_file(chess_file_data)

# Agregar ganador a una partida
def add_game_winner(game_id):
    try:
        # Obtener datos del juego
        chess_file_data = get_chess_file_data()
        game_data = chess_file_data['games'][str(game_id)]
        # Preguntar por los datos del jugador
        player_id = input('Escribe el número del jugador: ')
        # Obtener datos del jugador
        player = get_player_data(player_id)

        # Asegurarse de que existe el jugador
        if player != None:
            # Actualizar datos del juego
            game_data['winner'] = player
            # Actualizar datos de los juegos
            chess_file_data['games'][str(game_id)] = game_data
            # Guardar datos
            save_chess_file(chess_file_data)
            # Imprimir mensaje
            print('El ganador de la partida {} es {}'.format(game_id, player))
    except KeyError:
        # Imprimir un error
        print('No hay datos de ese juego')

# Obtener los datos de una partida
def get_game_data(game_id):
    try:
        # Obtener datos del juego
        chess_file_data = get_chess_file_data()
        game_data = chess_file_data['games'][str(game_id)]
        # Imprimir datos del juego
        print(game_data)
    except KeyError:
        print('No hay datos de esa partida')

# Guardar datos al archivo de ajedrez
def save_chess_file(chess_file_data):
    with open('chess.json', 'r+') as chess_file:
        # Guardar datos
        json.dump(chess_file_data, chess_file, ensure_ascii=False)

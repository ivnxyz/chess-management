# Importar dependencias
import os
from players import *
from games import *

# Imprimir menú para que se eliga una opción
def show_menu():
    print('''
        ¿Qué quieres hacer?

        [1].- Agregar una nueva partida
        [2].- Agregar ganador a una partida
        [3].- Obtener datos de una partida
        [4].- Obtener datos de un jugador
        [5].- Salir
    ''')

# Punto de entrada del programa
if __name__ == '__main__':
    # Limpiar consola
    os.system('clear')

    # Obtener path del archivo de partidas
    exists = os.path.isfile('./chess.json')

    # Asegurarse de que no hay un archivo de partidas ya creado
    if exists:
        while True:
            #Imprimir menú
            show_menu()
            choice = input('')

            # Limpiar consola
            os.system('clear')

            # Evaluar decisión
            if choice == '1':
                # Pedir el número de cada jugador
                player_one_id = input('Escribe el número del jugador 1: ')
                player_two_id = input('Escribe el número del jugador 2: ')
                game_id = input('Escribe el número de juego: ')
                start_new_match(player_one_id, player_two_id, game_id)
            elif choice == '2':
                # Pedir número del juego
                game_id = input('Escribe el número de juego: ')
                add_game_winner(game_id)
            elif choice == '3':
                # Pedir número del juego
                game_id = input('Escribe el número de juego: ')
                get_game_data(game_id)
            elif choice == '4':
                # Obtener datos de un jugador
                player_id = input('Escribe el número de jugador: ')
                player = get_player_data(player_id)
                # Asegurarse de que existe el jugador
                if player_id != None:
                    print('El jugador {} es {}'.format(player_id, player))
            elif choice == '5':
                break
            else:
                print(chalk.red('No conozco esa opción'))
                continue
    else:
        # Importar lista de jugadores
        players = import_players()
        # Guardar lista de jugadores
        save_players_data(players)

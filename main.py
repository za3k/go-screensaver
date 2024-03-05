import requests
from pprint import pprint

AIDEN_URL="https://online-go.com/api/v1/players/946392/games"

aiden_json = requests.get(AIDEN_URL).json()
games = aiden_json["results"]
first_game = games[0]
first_game_id = first_game["id"]
game_url = "https://online-go.com/api/v1/games/{}".format(first_game_id)
sgf_url = "https://online-go.com/api/v1/games/{}/sgf".format(first_game_id)

game_json = requests.get(game_url).json()
moves = game_json["gamedata"]["moves"]
handicap = game_json["gamedata"]["handicap"]

sgf = requests.get(sgf_url).content
with open("aiden.sgf", "wb") as f:
    f.write(sgf)


def display_board(b):
    import colorama
    for row in b:
        for spot in row:
            print(colorama.Fore.RESET + colorama.Style.NORMAL, end='')
            if spot == "white":
                print(colorama.Style.BRIGHT + "● ", end='')
            if spot == "black":
                print("○ ",end='')
            if spot == "blank":
                print(colorama.Style.BRIGHT + colorama.Fore.BLACK + "· ",end='')
        print()

def wait_a_bit():
    import time
    time.sleep(0.25)

def clear_screen():
    import subprocess, os
    subprocess.call('clear' if os.name == 'posix' else 'cls')

board = [['blank']*19 for _ in range(19)]
turn = 'black'
for move in moves:
    board[move[1]][move[0]] = turn
    turn = {"black": "white", "white": "black"}[turn]
    clear_screen()
    display_board(board)
    wait_a_bit()

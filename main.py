from os import system
from time import sleep

def clear_output():
    sleep(5)
    system('cls')

def display_board(board):

    #We need to print a board.

    top_and_bottom = "-------------------"
    pretty_lines = "|-----|-----|-----|"

    clear_output()
    print(top_and_bottom)
    for i in range(1, 10, 3):
        print('|  ' + board[i] + '  |  ' + board[i+1] + '  |  ' + board[i+2] + '  |  ')
        if i < 7:
            print(pretty_lines)
    print(top_and_bottom)

def player_input():

    #Take in player input.

    player_one = None
    player_two = None

    marker = ''

    while marker != 'X' and marker != 'O':
        marker = input("Player 1, chose X or O : ")

    player_one = marker

    if player_one == 'X':
        player_two = 'O'
    else:
        player_two = "X"

    return (player_one, player_two)

def update_board():

    #Place their input on the board.

    pass

def game_state():

    #Check if the game is won,tied, lost, or ongoing.

    pass

def replay():

    #Ask if players want to play again.

    pass

def main():
    
    #Repeat c and d until the game has been won or tied.
    
    pass




#player_one_marker, player_two_marker = player_input()

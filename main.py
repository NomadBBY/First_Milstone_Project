from time import sleep
from os import system
from random import randint

def clear_output():
    system('cls')

def display_board(board):

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
    
    marker = ''

    while not (marker == "X" or marker == "O"):
        marker = input("Player One: Chose X or O: ").upper()

    if marker == "X":
        return ("X", "O")
    else:
        return ("O", "X")

def place_marker(board, marker, position):
    
    board[position] = marker

def win_check(board, mark):

    board_=[el==mark for el in board]
    if(any([
        all(board_[1:4]),
        all(board_[4:7]),
        all(board_[7:10]),
        all(board_[slice(1,8,3)]),
        all(board_[slice(2,9,3)]),
        all(board_[slice(3,10,3)]),
        all(board_[slice(1,10,4)]),
        all(board_[slice(3,8,2)])
    ])):
        return True
    return False

def chose_first():

    coinflip = randint(0,1)
    
    if coinflip == 0:
        return "Player 1"
    else:
        return "Player 2"

def space_check(board, position):

    return board[position] == " "

def full_board_check(board):

    for i in range(1,10):
        if space_check(board, i):
            return False 
        
    return True

def player_choice(board):

    position = 0

    while position not in list(range(1,10)) or not space_check(board, position):
        position = int(input("Choose a position: (1-9) :"))

    return position

def replay():
    
    choice = input("Play again? Enter Yes or No").capitalize()

    return choice == "Yes"

test_board = [' '] * 10
# display_board(test_board)
# player1, player2 = player_input()
display_board(test_board)
print((win_check(test_board, "X")))

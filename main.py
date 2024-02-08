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
    
    choice = input("Play again? Enter Yes or No : ").capitalize()

    return choice == "Yes"

def main():

    print("Welcome to Tic Tac Toe!")
    print()

    while True:

        the_board = [' '] * 10
        player1_marker, player2_marker = player_input()

        turn = chose_first()
        print(turn + " Will go first")

        play_game = input("Are you ready to play? : (Yes/No) ").lower()

        if play_game == "yes":
            game_on = True
        else:
            game_on = False

        while game_on:

            if turn == "Player 1":

                display_board(the_board)
                print("It's player One turn!")
                position = player_choice(the_board)
                place_marker(the_board, player1_marker,position)

                if win_check(the_board, player1_marker):
                    display_board(the_board)
                    print("Player 1 has won!")
                    game_on = False
                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print("The game is a tie!")
                        game_on = False
                    else:
                        turn = "Player 2"
            else:

                display_board(the_board)
                print("It's player Two turn!")
                position = player_choice(the_board)
                place_marker(the_board, player2_marker,position)

                if win_check(the_board, player2_marker):
                    display_board(the_board)
                    print("Player 2 has won!")
                    game_on = False
                else:
                    if full_board_check(the_board):
                        display_board(the_board)
                        print("The game is a tie!")
                        game_on = False
                    else:
                        turn = "Player 1"

        if not replay():
            break

main()

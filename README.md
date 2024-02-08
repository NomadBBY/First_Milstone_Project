# Tic Tac Toe Game

This is a simple Tic Tac Toe game implemented in Python. It allows two players to play against each other on the console.

## How to Run

Make sure you have Python installed on your system.

To run the game, simply execute the Python script `tic_tac_toe.py` using your Python interpreter.

```bash
python tic_tac_toe.py
```

## Game Instructions

1. The game starts by asking Player One to choose their marker, either 'X' or 'O'.
2. Player One is randomly chosen to start the game.
3. Players take turns placing their markers ('X' or 'O') on a 3x3 board.
4. The first player to get three of their markers in a row (horizontally, vertically, or diagonally) wins the game.
5. If all the positions on the board are filled without any player winning, the game ends in a tie.
6. After the game ends, players have the option to replay.

## Functions

1. `display_board(board)`: Displays the current state of the game board.
2. `player_input()`: Allows Player One to choose their marker ('X' or 'O').
3. `place_marker(board, marker, position)`: Places the marker on the specified position on the board.
4. `win_check(board, mark)`: Checks if a player has won the game.
5. `chose_first()`: Randomly selects which player goes first.
6. `space_check(board, position)`: Checks if a position on the board is empty.
7. `full_board_check(board)`: Checks if the board is full.
8. `player_choice(board)`: Allows the current player to choose a position on the board to place their marker.
9. `replay()`: Asks players if they want to play again.
10. `main()`: Main function that controls the flow of the game.

## Enjoy the Game!

Have fun playing Tic Tac Toe! If you encounter any issues or have suggestions for improvements, feel free to let us know.

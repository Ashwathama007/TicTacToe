# Tic Tac Toe Game in Python

## Description
This project is a simple implementation of the classic Tic Tac Toe game, designed to be played in the terminal. It provides a fun way to practice Python programming while creating an interactive game.

## Features
- Two-player mode.
- Input validation to ensure correct moves.
- Display of the game board after each move.
- Detection of win, lose, or draw conditions.
- Restart option after the game ends.

## Requirements
- Python 3.x

## How to Run
1. **Clone the Repository:**
    ```bash
    git clone https://github.com/Ashwathama007/TicTacToe.git
    cd TicTacToe
    ```

2. **Run the Game:**
    ```bash
    python3 main.py
    ```

## How to Play
1. The game is played on a 3x3 grid.
2. Player 1 is 'X' and Player 2 is 'O'.
3. Players take turns to place their marks in empty cells by entering the corresponding number for the cell (0-8).
4. The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner.
5. If all 9 cells are filled and no player has 3 marks in a row, the game is a draw.
6. After the game ends, players have the option to restart the game.

## Example
Here's a sample interaction with the game:
```
Welcome to Tic Tac Toe
 0 | 1 | 2 
---|---|---
 3 | 4 | 5 
---|---|---
 6 | 7 | 8 
X's Turn
Please enter a value :2
 0 | 1 | X 
---|---|---
 3 | 4 | 5 
---|---|---
 6 | 7 | 8 
O's Turn
Please enter a value :1
 0 | O | X 
---|---|---
 3 | 4 | 5 
---|---|---
 6 | 7 | 8 
... (game continues)
```

## Code Explanation
The core logic of the game is implemented in `main.py`. The main components include:

- **printBoard:** Function to display the current state of the game board.
- **winner:** Function to check if a player has won or if it is a draw.
- **checking_validity** Function to check if the number typed has already been occupied or not and if the typed number is a valid number
- **start** The loop that runs the game, alternating turns between players and checking for win/draw conditions.

## Acknowledgments
This project was inspired by the classic Tic Tac Toe game and various online tutorials on Python game development. 
The initial code was taken from the CodeWithHarry YouTube channel, but additional features and improvements have been added to enhance the game.

---

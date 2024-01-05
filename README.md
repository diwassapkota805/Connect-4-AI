# Max-Connect-4 Game

## Overview
This project implements an agent for playing the max-connect-4 game, utilizing a depth-limited version of the minimax algorithm with alpha-beta pruning. The game takes place on a 6 x 7 grid and involves two players, designated as player A and player B, with their presence on the board represented by the numbers 1 and 2. Players take turns placing pieces at empty spots on the board.

## Files
1. **maxconnect4.py:** Python script that sets up the game board and calls the AI algorithm to predict the next best move.
2. **Maxconnect4game.py:** Defines a class managing the connect-four game state. It contains AI algorithms and an evaluation function.
3. **input1.txt:** Input file with an empty board.
4. **input2.txt:** Input file with a partially filled board.

## Modes

### Interactive Mode
- To play against the computer/AI (computer makes the first move):
  ```bash
  python maxconnect4.py interactive input1.txt computer-next 2

### One-Move Mode
- Make a single move and terminate, outputting the result:
  ```bash
  python maxconnect4.py one-move input1.txt output.txt 2

## Algorithm Overview

The algorithm employs depth-limited minimax with alpha-beta pruning in max-connect-4. Key components include:

- **Evaluation (`utility`):**
  - Weighs fours, threes, and twos (1000, 100, 10).
  
- **Move Selection:**
  - Plays in the column with the highest utility.

- **Depth-Limited Minimax:**
  - Efficient exploration with depth limitation.
  - Uses alpha-beta pruning for computational efficiency.
  
Implemented in `alphaBetaPruning` within `MaxConnect4Game.py`.

## Future Enhancements
- a graphical interface would be nice :)

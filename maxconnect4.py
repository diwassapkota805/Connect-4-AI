#!/usr/bin/env python
"""
Copyright (C) 2016 Chris Conly (chris.conly@uta.edu)

"""
import sys
from MaxConnect4Game import *

# function to play one move and print the output to the output file
def oneMoveGame(currentGame, depth):
    if currentGame.pieceCount == 42:    # is the board full already?
        print('BOARD')
        currentGame.printGameBoard()
        sys.exit(0)

    currentGame.aiPlay(currentGame.gameBoard, depth) # Make a move (only random is implemented)

    print('Game state after move:')
    currentGame.printGameBoard()

    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))

    currentGame.printGameBoardToFile()
    currentGame.gameFile.close()

# function to play the game interactively (player vs computer)
def interactiveGame(currentGame, turn, depth):
    while currentGame.pieceCount < 42:  # if the board is not full yet
        if turn == "computer-next":  # if it is computer-turn, then make a move using the minimax algorithm
            print("Computer is making a move.....")
            currentGame.aiPlay(currentGame.gameBoard, depth)
            currentGame.gameFile = open("computer.txt", 'w')
            currentGame.printGameBoard()
            currentGame.printGameBoardToFile()
            currentGame.gameFile.close()
            # change the turn
            if currentGame.currentTurn == 1:
                currentGame.currentTurn = 2
            elif currentGame.currentTurn == 2:
                currentGame.currentTurn = 1
            turn = "human-next"
            continue
       
        else:   # if it is human-turn, then ask the user to make a move
            print("Human is making a move.....")
            user_input = input("Enter the column number (0-6):")

            # # if the user input is empty or not a number, then ask the user to enter again
            # if not user_input:
            #     print("Invalid input. Please enter a number beetwen 0 and 6")
            #     continue
            
            try:
                user_input = int(user_input)
            except ValueError:
                print("Invalid input. Please enter a number beetwen 0 and 6")
                continue

            if  user_input < 0 or user_input > 6:
                print("Invalid input. Please enter a number beetwen 0 and 6")
                continue

            if not currentGame.playPiece(user_input):
                print("this column is full. Please enter another column number")
                continue
            
            print('move %d: Player %d, column %d\n' % (currentGame.pieceCount, currentGame.currentTurn, user_input))
            currentGame.gameFile = open("human.txt", 'w')
            currentGame.printGameBoard()
            currentGame.printGameBoardToFile()
            currentGame.gameFile.close()

            # change the turn
            if currentGame.currentTurn == 1:
                currentGame.currentTurn = 2
            elif currentGame.currentTurn == 2:
                currentGame.currentTurn = 1
            turn = "computer-next"
            continue
    
    # after the game loop, check the score and print the winner
    currentGame.countScore()
    print('Score of Player 1 = %d, Score of Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))
    if currentGame.player1Score > currentGame.player2Score:
        print("Player 1 wins")
    elif currentGame.player1Score < currentGame.player2Score:
        print("Player 2 wins")
    else:
        print("It is a tie")
    sys.exit(0)

# main function
def main(argv):
    # Make sure we have enough command-line arguments
    if len(argv) != 5:
        print ('Four command-line arguments are needed:')
        print('Usage: %s interactive [input_file] [computer-next/human-next] [depth]' % argv[0])
        print('or: %s one-move [input_file] [output_file] [depth]' % argv[0])
        sys.exit(2)

    game_mode, inFile = argv[1:3]

    if not game_mode == 'interactive' and not game_mode == 'one-move':
        print('%s is an unrecognized game mode' % game_mode)
        sys.exit(2)

    currentGame = maxConnect4Game() # Create a game

    # Try to open the input file
    try:
        currentGame.gameFile = open(inFile, 'r')
    except IOError:
        sys.exit("\nError opening input file.\nCheck file name.\n")

    # Read the initial game state from the file and save in a 2D list
    file_lines = currentGame.gameFile.readlines()
    currentGame.gameBoard = [[int(char) for char in line[0:7]] for line in file_lines[0:-1]]
    currentGame.currentTurn = int(file_lines[-1][0])
    currentGame.gameFile.close()

    print('\nMaxConnect-4 game\n')
    print('Game state before move:')
    currentGame.printGameBoard()

    # Update a few game variables based on initial state and print the score
    currentGame.checkPieceCount()
    currentGame.countScore()
    print('Score: Player 1 = %d, Player 2 = %d\n' % (currentGame.player1Score, currentGame.player2Score))
    

    if game_mode == 'interactive':
        interactiveGame(currentGame, argv[3], int(argv[4])) # Be sure to pass whatever else you need from the command line
    else: # game_mode == 'one-move'
        # Set up the output file
        outFile = argv[3]
        try:
            currentGame.gameFile = open(outFile, 'w')
        except:
            sys.exit('Error opening output file.')
        oneMoveGame(currentGame, int(argv[4])) # Be sure to pass any other arguments from the command line you might need.


if __name__ == '__main__':
    main(sys.argv)

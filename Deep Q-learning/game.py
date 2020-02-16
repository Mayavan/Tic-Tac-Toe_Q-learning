'''
--------------------
Functions Used:
--------------------
drawBoard(self, board) - draws the current board on the console
inputPlayerLetter - Gets the Letter you
makeMove(self, board, letter, move) - update move to board array
isWinner(self, board, letter) - check if letter given is winner
getBoardCopy(self, board)
isSpaceFree(self, board, move)
getPlayerMove(self, board)
chooseRandomMoveFromList(self, board, movesList)
getTraditionalComputerMove(self, board, computerLetter)
isBoardFull(self, board)
'''

# Tic Tac Toe
import random
from math import pow

from NeuralNetwork import NeuralNetwork


class Game:
    def play(self, player_1="computer", player_2="AI", episodes=100, alpha=0.3, gamma=0.9, epsilon=0.5):
        print('Welcome to Tic Tac Toe!')

        player1Letter = 'X'
        player2Letter = 'O'

        count = -1
        win = 0
        loss = 0
        tie = 0

        self.model = NeuralNetwork()

        self.previousStatePlayer1 = 0
        self.previousActionPlayer1 = 0
        self.previousStatePlayer2 = 0
        self.previousActionPlayer2 = 0

        while True:
            count = count + 1
            if count == episodes:
                return win, loss, tie
            print("-------------------------------------------")
            print("Episode: ", count + 1)
            print("-------------------------------------------")
            # Reset the board
            theBoard = [' '] * 10
            theBoard[0] = "A"
            turn = 'player1'
            print('The ' + turn + ' will go first.')
            gameIsPlaying = True

            while gameIsPlaying:
                if turn == 'player1':
                    # Player1's turn.
                    if player_1 == "AI":
                        move = self.getAImove(theBoard)
                    elif player_1 == "computer":
                        move = self.getTraditionalComputerMove(theBoard, player1Letter)
                    elif player_1 == "human":
                        self.drawBoard(theBoard)
                        move = self.getPlayerMove(theBoard)

                    # Store value of current state for QUpdate
                    boardindex = self.getBoardCopy(theBoard[1:])
                    self.previousStatePlayer1 = self.getstate(boardindex)
                    self.previousActionPlayer1 = move - 1  # in index form

                    self.makeMove(theBoard, player1Letter, move)

                    if self.isWinner(theBoard, player1Letter):
                        self.drawBoard(theBoard)
                        print('Hooray! Player1 won the game!')
                        gameIsPlaying = False
                        loss = loss + 1
                    else:
                        if self.isBoardFull(theBoard):
                            self.drawBoard(theBoard)
                            print('The game is a tie!')
                            tie = tie + 1
                            break
                        else:
                            turn = 'player2'



                else:
                    # Player2's turn.
                    if player_2 == "AI":
                        move = self.getAImove(theBoard)
                    elif player_2 == "computer":
                        move = self.getTraditionalComputerMove(theBoard, player2Letter)
                    elif player_2 == "human":
                        self.drawBoard(theBoard)
                        move = self.getPlayerMove(theBoard)

                    # Store value of current state for QUpdate
                    boardindex = self.getBoardCopy(theBoard[1:])
                    self.previousStatePlayer2 = self.getstate(boardindex)
                    self.previousActionPlayer2 = move - 1  # in index form

                    self.makeMove(theBoard, player2Letter, move)

                    if self.isWinner(theBoard, player2Letter):
                        self.drawBoard(theBoard)
                        print('Hooray! Player2 won the game!')
                        gameIsPlaying = False
                        win = win + 1
                    else:
                        if self.isBoardFull(theBoard):
                            self.drawBoard(theBoard)
                            print('The game is a tie!')
                            tie = tie + 1
                            break
                        else:
                            turn = 'player1'


    def drawBoard(self, board):
        # This function prints out the board that it was passed.

        # "board" is a list of 10 strings representing the board (ignore index 0)
        print('   |   |')
        print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
        print('   |   |')

    def playAgain(self):
        # This function returns True if the player wants to play again, otherwise it returns False.
        print('Do you want to play again? (yes or no)')
        return input().lower().startswith('y')

    def makeMove(self, board, letter, move):
        board[move] = letter

    def isWinner(self, bo, le):
        # Given a board and a player's letter, this function returns True if that player has won.
        # We use bo instead of board and le instead of letter so we don't have to type as much.
        return ((bo[7] == le and bo[8] == le and bo[9] == le) or  # across the top
                (bo[4] == le and bo[5] == le and bo[6] == le) or  # across the middle
                (bo[1] == le and bo[2] == le and bo[3] == le) or  # across the bottom
                (bo[7] == le and bo[4] == le and bo[1] == le) or  # down the left side
                (bo[8] == le and bo[5] == le and bo[2] == le) or  # down the middle
                (bo[9] == le and bo[6] == le and bo[3] == le) or  # down the right side
                (bo[7] == le and bo[5] == le and bo[3] == le) or  # diagonal
                (bo[9] == le and bo[5] == le and bo[1] == le))  # diagonal

    def getBoardCopy(self, board):
        # Make a duplicate of the board list and return it the duplicate.
        dupeBoard = []

        for i in board:
            dupeBoard.append(i)
        return dupeBoard

    def isSpaceFree(self, board, move):
        # Return true if the passed move is free on the passed board.
        return board[move] == ' '

    def getPlayerMove(self, board):
        # Let the player type in his move.
        move = ' '
        while move not in '1 2 3 4 5 6 7 8 9'.split() or not self.isSpaceFree(board, int(move)):
            print('What is your next move? (1-9) Use your numberpad to make a move and press enter.')
            move = input()
        return int(move)

    def chooseRandomMoveFromList(self, board, movesList):
        # Returns a valid move from the passed list on the passed board.
        # Returns None if there is no valid move.
        possibleMoves = []
        for i in movesList:
            if self.isSpaceFree(board, i):
                possibleMoves.append(i)

        if len(possibleMoves) != 0:
            return random.choice(possibleMoves)
        else:
            return None

    def getTraditionalComputerMove(self, board, computerLetter):
        # Given a board and the computer's letter, determine where to move and return that move.
        if computerLetter == 'X':
            playerLetter = 'O'
        else:
            playerLetter = 'X'

        # Here is our algorithm for our Tic Tac Toe AI:
        # First, check if we can win in the next move
        for i in range(1, 10):
            copy = self.getBoardCopy(board)
            if self.isSpaceFree(copy, i):
                self.makeMove(copy, computerLetter, i)
                if self.isWinner(copy, computerLetter):
                    return i

        # Check if the player could win on his next move, and block them.
        for i in range(1, 10):
            copy = self.getBoardCopy(board)
            if self.isSpaceFree(copy, i):
                self.makeMove(copy, playerLetter, i)
                if self.isWinner(copy, playerLetter):
                    return i

        # Try to take one of the corners, if they are free.
        move = self.chooseRandomMoveFromList(board, [1, 3, 7, 9])
        if move != None:
            return move

        # Try to take the center, if it is free.
        if self.isSpaceFree(board, 5):
            return 5

        # Move on one of the sides.
        return self.chooseRandomMoveFromList(board, [2, 4, 6, 8])

    def getAImove(self, board):
        # In Q learning class 0-8 are the index of move

        copy = self.getBoardCopy(board[1:])
        state = self.getstateArray(copy)

        possible_moves = self.getPossibleMoves(copy)
        print("The possible moves for AI are:{}".format(possible_moves))
        move = self.model.getmove(state, possible_moves)

        print("The move made is:{}".format(move))

        return move + 1

    def getPossibleMoves(self, board):
        possible = []
        for i in range(len(board)):
            if board[i] == " ":
                possible.append(i)
        return possible

    def isBoardFull(self, board):
        # Return True if every space on the board has been taken. Otherwise return False.
        for i in range(1, 10):
            if self.isSpaceFree(board, i):
                return False
        return True

    def getstate(self, copy):
        state = 0
        for i, letter in enumerate(copy):
            if letter == " ":
                state = state + 0
            elif letter == "X":
                state = state + pow(3, i)
            else:
                state = state + 2 * pow(3, i)
        return int(state)

    def getstateArray(self, copy):
        state = []
        for i, letter in enumerate(copy):
            if letter == " ":
                state.append(0)
            elif letter == "X":
                state.append(1)
            else:
                state.append(2)
        return state

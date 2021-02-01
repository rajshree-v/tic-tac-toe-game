"""
Tic Tac Toe Player
"""

import math
import copy
import sys
import random

branches = []

X = "X"
O = "O"
EMPTY = "_"


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]] 


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    xcount, ocount = 0, 0
    for row in board:
        xcount += row.count(X)
        ocount += row.count(O)
    if xcount > ocount:
        return O
    elif xcount == 0 and ocount == 0:
        return X
    elif xcount == ocount:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()

    if not terminal(board):
        for i in range(3):
            for j in range(3):
                if board[i][j] is EMPTY:
                    val = (i, j)
                    possible_actions.add(val)

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    newBoard = copy.deepcopy(board)
    try:
        if newBoard[action[0]][action[1]] != EMPTY:
            raise IndexError
        else:
            newBoard[action[0]][action[1]] = player(newBoard)
            return newBoard
    except IndexError:
        print('Spot occupied')


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    columns = []
    for row in board:
        xcount = row.count(X)
        ocount = row.count(O)
        if xcount == 3:
            return X
        if ocount == 3:
            return O

    for j in range(len(board)):
        column = [row[j] for row in board]
        columns.append(column)
    
    for j in columns:
        xcounter = j.count(X)
        ocounter = j.count(O)
        if xcounter == 3:
            return X
        if ocounter == 3:
            return O
    
    if board[0][0] == O and board[1][1] == O and board[2][2] == O:
        return O
    if board[0][0] == X and board[1][1] == X and board[2][2] == X:
        return X
    if board[0][2] == O and board[1][1] == O and board[2][0] == O:
        return O
    if board[0][2] == X and board[1][1] == X and board[2][0] == X:
        return X

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    emptyCounter = 0
    for row in board:
        emptyCounter += row.count(EMPTY)
    if emptyCounter == 0:
        return True
    elif winner(board) is not None:
        return True
    else:
        return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    if player(board) == O:
        v = math.inf
        for action in actions(board):
            move = max_value(result(board, action))
            if move < v:
                v = move
                bestMove = action

    else:
        v = -math.inf
        for action in actions(board):
            move = min_value(result(board, action))
            if move > v:
                v = move
                bestMove = action
    
    return bestMove


def max_value(board):
    if terminal(board):
        return utility(board)
    v_max = -math.inf
    for action in actions(board):
        v_max = max(v_max, min_value(result(board, action)))
    return v_max


def min_value(board):
    if terminal(board):
        return utility(board)
    v_min = math.inf
    for action in actions(board):
        v_min = min(v_min, max_value(result(board, action)))
    return v_min

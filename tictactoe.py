"""
Tic Tac Toe Player
"""
import copy
import math

X = "X"
O = "O"
EMPTY = None


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
    counter_x, counter_o = 0
    for each_row in board:
        for cell in each_row:
            if cell == X:
                counter_x += 1
            elif cell == O:
                counter_o += 1
    if counter_x > counter_o:
        return O
    else:

        return X


    raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action_set = set()
    for row_index, row in enumerate(board):
        for cell_index, cell in enumerate(row):
            if cell not in (X, O):
                action_set.add(row_index, cell_index)
    return action_set
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise NotImplementedError
    row_index, cell_index = action
    board_copy = copy.deepcopy(board)
    board_copy[row_index][cell_index] = player(board)

def CheckRow(board, player):
    for row in range(len(board)):
        if board[row][0] == player and board[row][1] == player and board[row][2] == player:
            return True
        return False

def CheckCol(board, player):
    for col in range(len(board)):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True
        return False
def CheckFirstDigit(board,player):
    count = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if row == col and board[row][col] == player:
                count +=1
    if count == 3:
        return True
    else:
        return False

def CheckSecondDigit(board, player):
    count = 0
    for row in range(len(board)):
        for col in range(len(board[row])):
            if(len(board)) - row - 1 == col and board[row][col] == player:
                count +=1
    if count == 3:
        return True
    else:
        return False
def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if CheckRow(board,X) or CheckCol(board,X) or CheckFirstDigit(board,X) or CheckSecondDigit(board, X):
        return X
    elif CheckRow(board, O) or CheckCol(board, O) or CheckFirstDigit(board, O) or CheckSecondDigit(board, O):
        return O
    else:
        return None
def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X:
        return True
    if winner(board) == O:
        return True
    for row in range(len(board)):
        for col in range(len(board[row])):
            if board[row][col] == EMPTY:
                return False
    return True


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
def max_value(board):
    v = -math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v
def min_value(board):
    v = math.inf
    if terminal(board):
        return utility(board)
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v
def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    elif player(board) == X:
        plays = []
        for action in actions(board):
            plays.append([min_value(result(board,action)),action])
        return sorted(plays, key=lambda x: x[0], reverse=True)[0][1]
    elif player(board) == O:
        plays = []
        for action in actions(board):
            plays.append([max_value(result(board,action)),action])
        return sorted(plays, key=lambda x: x[0])[0][1]
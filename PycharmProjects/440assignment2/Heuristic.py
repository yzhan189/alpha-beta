import random
import numpy as np

def defensive1(board,turn):
    remain = len(board.player0) if  turn is 0 else len(board.player1)
    return 2*(remain) + random.random()

def offensive1(board,turn):
    remain = len(board.player0) if  turn is 1 else len(board.player1)
    return 2*(30 - remain) + random.random()

# the closet distance their pieces from my home, the more the better
def defensive2(board,turn):
    pieces = board.player0 if turn is 1 else board.player1
    myHome = 0 if turn is 0 else 7

    values = np.array([piece.position[0] for piece in pieces])
    if values.size is 0:
        return 0

    return min(abs(values-myHome))*100

# go to op home aggressively
# the distance my pieces from my home, further the better
def offensive2(board,turn):
    pieces = board.player0 if turn is 0 else board.player1
    myHome = 0 if turn is 0 else 7

    values = np.array([piece.position[0] for piece in pieces])
    if values.size is 0:
        return 0

    return max(abs(values-myHome))*100+offensive1(board,turn)






import random
import numpy as np

def defensive1(board,turn):
    remain = len(board.player0) if  turn is 0 else len(board.player1)
    return 2*(remain) + random.random()

def offensive1(board,turn):
    remain = len(board.player0) if  turn is 1 else len(board.player1)
    return 2*(30 - remain) + random.random()

def defDistance(board,turn):
    pieces = board.player0 if turn is 1 else board.player1
    myHome = 0 if turn is 0 else 7

    values = np.array([piece.position[0] for piece in pieces])
    if values.size is 0:
        return 0
    return sum((abs(values - myHome)) ** 4)

def offDistance(board,turn):
    pieces = board.player0 if turn is 0 else board.player1
    myHome = 0 if turn is 0 else 7

    values = np.array([piece.position[0] for piece in pieces])
    if values.size is 0:
        return 0

    return sum((abs(values-myHome))**4)


# the closet distance their pieces from my home, the more the better
def defensive2(board,turn):


    return 3*defDistance(board,turn)+ offDistance(board,turn)+random.random()

# go to op home aggressively
# the distance my pieces from my home, further the better
def offensive2(board,turn):


    return  defDistance(board,turn)+ 3*offDistance(board,turn) + random.random()






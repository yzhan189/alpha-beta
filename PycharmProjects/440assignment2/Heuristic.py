import random

def defensive1(board,turn):
    remain = len(board.player0) if  turn is 0 else len(board.player1)
    return 2*(remain) + random.random()

def offensive1(board,turn):
    remain = len(board.player0) if  turn is 1 else len(board.player1)
    return 2*(30 - remain) + random.random()

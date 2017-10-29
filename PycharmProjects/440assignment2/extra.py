from recBorad import RecBoard as Board
from search import minimax,alpha_beta,alpha_beta2,alpha_beta3
from Heuristic import defensive1,offensive1,defensive2,offensive2
import time
import numpy as np


board = Board()

print("extra")
s = time.time()
winner = -1
turn =0
playerExpanded = np.array([0, 0])
totalTurn = 0
while (winner == -1 ):


    _, board, expanded = alpha_beta(turn, board, 4, offensive1, True, -np.inf, np.inf)


    playerExpanded[turn] += expanded

    turn = 1 - turn
    winner = board.checkWinner()
    totalTurn += 1
    board.print()

e = time.time()

print("\n\nWinner is " + str(winner))
print("\nTotal turns: " + str(totalTurn))
print("\ntime: " + ("%.3f" % (e - s)) + 's')
print("\nAverage node expended: " + str(playerExpanded//(totalTurn/2)))
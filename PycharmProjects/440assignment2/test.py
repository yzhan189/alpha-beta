from Board import Board
from search import minimax,alpha_beta
from Heuristic import defensive1,offensive1
import time
import numpy as np

board = Board()
start = time.time()

turn = 0
winner = -1
count=0
playerExpanded=[0,0]

# 1
while (winner==-1 ):
    # both use defensive
    #if turn is 0:
    #    _, board, expanded = minimax(turn,board,3,offensive1,True)
    #else:
    #    _, board, expanded = alpha_beta(turn, board, 4, offensive1, True,-np.inf,np.inf)

    _, board, expanded = alpha_beta(turn, board, 4, offensive1, True, -np.inf, np.inf)
    playerExpanded[turn] += expanded

    turn = 1-turn
    winner = board.checkWinner()



board.print()
end = time.time()
print("Node expended: "+str(playerExpanded))

print("\ntime: ")
print("%.3f" % (end - start))



#print(winner)


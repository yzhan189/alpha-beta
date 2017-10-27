from Board import Board
from search import minimax,alpha_beta
from Heuristic import defensive1,offensive1

board = Board()
board.print()

turn = 0
winner = -1

#while(winner==-1):
#    _, board = minimax(turn,board,3,defensive1,True)
#    board.checkWinner()




board.move((1,0),(6,1))
board.print()
print(board.board[(1,0)])


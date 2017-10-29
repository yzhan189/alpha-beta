from Board import Board
from search import minimax,alpha_beta,alpha_beta2,alpha_beta3
from Heuristic import defensive1,offensive1,defensive2,offensive2
import time
import numpy as np
from recBorad import RecBoard


def run(MATCH_UP):


    board = Board()
    #board = RecBoard()
    s = time.time()

    turn = 0
    winner = -1
    playerExpanded=np.array([0,0])
    totalTurn = 0



    search0 = alpha_beta
    search1 = alpha_beta
    depth0 = 4
    depth1 = 4

    h0 = None
    h1 = None

    PLAYER_0_MESSAGE=''
    PLAYER_1_MESSAGE=''


    if MATCH_UP is 1:
        search0 = minimax
        depth0 = 3

        h0 = offensive1
        PLAYER_0_MESSAGE = 'Minimax (Offensive Heuristic 1)'

    if MATCH_UP in [2,4,6]:
        h0 = offensive2
        PLAYER_0_MESSAGE = 'Alpha-beta (Offensive Heuristic 2)'

    if MATCH_UP in [3,5]:
        h0 = defensive2
        PLAYER_0_MESSAGE = 'Alpha-beta (Defensive Heuristic 2)'

    if MATCH_UP is 6:
        h1 = defensive2
        PLAYER_1_MESSAGE = 'Alpha-beta (Defensive Heuristic 2)'

    if MATCH_UP in [1,3,4] :
        print(True)
        h1 = offensive1
        PLAYER_1_MESSAGE = 'Alpha-beta (Offensive Heuristic 1)'

    if MATCH_UP in [2,5] :
        h1 = defensive1
        PLAYER_1_MESSAGE = 'Alpha-beta (Defensive Heuristic 1)'


    print ("\nMatchup: "+ str(MATCH_UP) )
    print(PLAYER_0_MESSAGE+' at depth '+str(depth0)+
          '\n VS \n'+PLAYER_1_MESSAGE+' at depth '+str(depth1))


    while (winner==-1):

        if turn is 0:
            _, board, expanded = search0(turn,board,depth0,h0,True)
        else:
            _, board, expanded = search1(turn, board, depth1, h1, True)
        #board.print()
        #_, board, expanded = alpha_beta3(turn, board, 4, offensive1, True,totalTurn, -np.inf, np.inf)

        #    _, board, expanded = minimax(turn, board, 3, offensive1, True)
        playerExpanded[turn] += expanded

        turn = 1-turn
        winner = board.checkWinner2()
        totalTurn+=1

    print()
    board.print()
    e = time.time()


    print("\n\nWinner is "+str(winner) )
    print("\nTotal turns: "+str(totalTurn))
    print("\nAverage node expended: " + str(playerExpanded // (totalTurn / 2)))
    print("\ntime: " + ("%.3f" % (e - s))+'s')



#print(winner)
#test ==========

# board = Board()
# winner = -1
# turn =0
# playerExpanded = np.array([0, 0])
# totalTurn = 0
# while (winner == -1 and  totalTurn<20):
#     s = time.time()
#     _, board, expanded = alpha_beta2(turn, board, 4, offensive1, True, -np.inf, np.inf)
#     e = time.time()
#     #print("with ordering ")
#     playerExpanded[turn] += expanded
#     #print("\ntime: " + ("%.3f" % (e - s))+'s')
#     #print("\nNode expended: "+str(expanded))
#     turn = 1 - turn
#     winner = board.checkWinner()
#     totalTurn += 1
#
# print("\n\nWinner is "+str(winner) )
# print("\nTotal turns: "+str(totalTurn))
# print("\nAverage node expended: " + str(playerExpanded // (totalTurn / 2)))
# print("\ntime: " + ("%.3f" % (e - s))+'s')

# board = Board()
# board.move((1,0),(4,0))
# board.move((1,1),(3,1))
# board.move((0,0),(4,4))
# board.move((0,4),(2,3))
# board.move((1,2),(5,3))
# board.move((1,3),(3,0))
# board.move((1,7),(3,3))
# board.move((1,6),(3,4))
# winner = -1
# turn =0
# playerExpanded = np.array([0, 0])
# totalTurn = 0
# s = time.time()
#
# while (winner == -1):
#
#     _, board, expanded = alpha_beta(turn, board, 3, offensive1, True)
#     #print("with out ordering ")
#     playerExpanded[turn] += expanded
#     #print("\ntime: " + ("%.3f" % (e - s))+'s')
#     #print("\nNode expended: "+str(expanded))
#     turn = 1 - turn
#     winner = board.checkWinner()
#     totalTurn += 1
#
# e = time.time()
# print("\n\nWinner is "+str(winner) )
# print("\nTotal turns: "+str(totalTurn))
# print("\nAverage node expended: " + str(playerExpanded // (totalTurn / 2)))
# print("\ntime: " + ("%.3f" % (e - s))+'s')
# depth = 3
#       o               3 max
#     /   \
#    o     o            2 min
#   / \   / \
#  o   o o   o          1 max
#           / \
#          o   o        0 min
# worst case = (3*16)^depth

import numpy as np
from Heuristic import defensive1,offensive1

def findBestMove(board):
    return


def getPossibleMoves(turn):
    return


# h is heuristic function, level = deep at starting point
def minimax(turn, board, level, h, isMax):

    bestBoard = board
    sumExpanded = 0
    # base case: node value is heuristic
    if level is 0:
        return h(board,turn),bestBoard, sumExpanded

    # recursive case:
    allMoves = board.getAllMoves(turn)

    if (isMax):
        maxValue = -np.inf
        for (oldP, newP) in allMoves:
            currBoard = board.copyMove(oldP,newP)
            currValue, _,expandedBelow = minimax(1-turn,currBoard,level-1,h,not isMax)
            sumExpanded += expandedBelow+1
            if currValue > maxValue:
                maxValue = currValue
                bestBoard = currBoard
        return maxValue,bestBoard, sumExpanded

    else:
        minValue = np.inf
        for (oldP, newP) in allMoves:
            currBoard = board.copyMove(oldP, newP)
            currValue, _,expandedBelow = minimax(1 - turn, currBoard, level - 1, h, not isMax)
            sumExpanded += expandedBelow+1
            if currValue < minValue:
                minValue = currValue
                bestBoard = currBoard
        return minValue, bestBoard, sumExpanded



def alpha_beta(turn, board,level,h,isMax,alpha,beta):
    bestBoard = board
    sumExpanded = 0

    if level is 0:
        return h(board,turn), bestBoard, sumExpanded

    # recursive case:
    allMoves = board.getAllMoves(turn)

    if (isMax):
        maxValue = -np.inf
        for (oldP, newP) in allMoves:
            currBoard = board.copyMove(oldP,newP)
            currValue, _,expandedBelow = alpha_beta(1-turn,currBoard,level-1,h,not isMax,alpha,beta)
            sumExpanded += expandedBelow+1
            if currValue > maxValue:
                maxValue = currValue
                bestBoard = currBoard

            # pruning part
            alpha = max(alpha,maxValue)
            if beta <= alpha:
                break

        return maxValue,bestBoard, sumExpanded

    else:
        minValue = np.inf
        for (oldP, newP) in allMoves:
            currBoard = board.copyMove(oldP, newP)
            currValue, _,expandedBelow = alpha_beta(1 - turn, currBoard, level - 1, h, not isMax,alpha,beta)
            sumExpanded += expandedBelow+1
            if currValue < minValue:
                minValue = currValue
                bestBoard = currBoard

            beta = min(beta,minValue)
            if beta <= alpha:
                break

        return minValue, bestBoard, sumExpanded

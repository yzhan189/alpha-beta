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




def alpha_beta(turn, board,level,h,isMax,alpha= -np.inf,beta=np.inf):
    bestBoard = board
    sumExpanded = 0

    if level is 0:
        return h(board,turn), bestBoard, sumExpanded

    # recursive case:
    allMoves = board.getAllMoves(turn)
    allMoves = np.array(allMoves)

    if (isMax):
        maxValue = -np.inf
        for (oldP, newP) in allMoves:
            currBoard = board.copyMove(oldP,newP)

            # if currBoard in dict:
            #     currValue = dict[currBoard]
            #     print("yeah")
            # else:
            currValue, _,expandedBelow = alpha_beta(1-turn,currBoard,level-1,h,not isMax,alpha,beta)
            sumExpanded += expandedBelow+1
                # dict[currBoard] = currValue

            if currValue > maxValue:
                maxValue = currValue
                bestBoard = currBoard

                # pruning part
                # idea: for pruning order, try to maximize alpha so that it break earlier
                alpha = max(alpha,maxValue)
                if beta <= alpha:
                    break

        return maxValue,bestBoard, sumExpanded

    else:
        minValue = np.inf
        for (oldP, newP) in allMoves:
            currBoard = board.copyMove(oldP, newP)

            # if currBoard in dict:
            #     currValue = dict[currBoard]
            # else:
            currValue, _,expandedBelow = alpha_beta(1 - turn, currBoard, level - 1, h, not isMax,alpha,beta)
            sumExpanded += expandedBelow+1
                #dict[currBoard] = currValue

            if currValue < minValue:
                minValue = currValue
                bestBoard = currBoard

                beta = min(beta,minValue)
                if beta <= alpha:
                    break

        return minValue, bestBoard, sumExpanded



def getBetterOrdering(allMoves,board,turn,h,rev):
    d = {}
    for (o,n) in allMoves:
        currBoard = board.copyMove(o,n)
        d[currBoard] = h(currBoard,turn)

    return sorted(d, key=d.get,reverse = rev)


def alpha_beta2(turn, board,level,h,isMax,alpha= -np.inf,beta=np.inf):
    bestBoard = board
    sumExpanded = 0

    if level is 0:
        return h(board,turn), bestBoard, sumExpanded

    # recursive case:
    allMoves = board.getAllMoves(turn)

    d = getBetterOrdering(allMoves, board, turn, h, isMax)
    if (isMax):
        maxValue = -np.inf
        for currBoard in d:
            currValue, _,expandedBelow = alpha_beta2(1-turn,currBoard,level-1,h,not isMax,alpha,beta)
            sumExpanded += expandedBelow+1
            if currValue > maxValue:
                maxValue = currValue
                bestBoard = currBoard

                # pruning part
                # idea: for pruning order, try to maximize alpha so that it break earlier
                alpha = max(alpha,maxValue)
                if beta <= alpha:
                    break

        return maxValue,bestBoard, sumExpanded

    else:
        minValue = np.inf
        for currBoard in d:
            currValue, _,expandedBelow = alpha_beta2(1 - turn, currBoard, level - 1, h, not isMax,alpha,beta)
            sumExpanded += expandedBelow+1
            if currValue < minValue:
                minValue = currValue
                bestBoard = currBoard

                beta = min(beta,minValue)
                if beta <= alpha:
                    break

        return minValue, bestBoard, sumExpanded



def alpha_beta3(turn, board,level,h,isMax,count,alpha= -np.inf,beta=np.inf):
    if count <20:
        return alpha_beta(turn, board,level,h,isMax)
    else:
        return alpha_beta2(turn, board, level, h, isMax)
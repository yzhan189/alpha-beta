from Worker import Worker
from Player import Player
import numpy as np

BOARD_SHAPE = (5,10)
class RecBoard:

    def __init__(self,new=True):

        self.board = np.empty(BOARD_SHAPE,dtype = object)
        self.player0 = list()
        self.player1 = list()
        if new:
            for j in range(BOARD_SHAPE[1]):
                # player0
                for i in [0]:
                    self.board[(i,j)] = Worker((i,j),0)
                    self.player0.append(self.board[(i,j)])
                # player1
                for i in [4]:
                    self.board[(i,j)] = Worker((i,j),1)
                    self.player1.append(self.board[(i, j)])

    def copyMove(self,oldP,newP):
        copy = RecBoard(False)
        for i in range(BOARD_SHAPE[0]):
            for j in range(BOARD_SHAPE[1]):
                if self.board[(i,j)] is not None:
                    if self.board[(i,j)].owner is 0:
                        copy.board[(i,j)] = Worker((i,j),0)
                        copy.player0.append(copy.board[(i,j)])
                    else:
                        copy.board[(i, j)] = Worker((i, j), 1)
                        copy.player1.append(copy.board[(i,j)])
        copy.move(oldP,newP)
        return copy


    # for 0, dir is +1, for 1, dir is -1
    # return ((x1,y1),(x2,y2))
    def getAllMoves(self,turn):
        direction = 0
        theList = None
        allMoves = list()
        if turn is 0:
            direction = 1
            theList = self.player0
        else:
            direction = -1
            theList = self.player1

        for worker in theList:
            oldP = worker.position
            (i,j) = oldP
            newP1 = (i+direction,j+1)
            newP2 = (i+direction,j-1)
            newP3 = (i+direction,j)

            if self.isValidMove(oldP,newP1,False):
                allMoves.append( ((i,j),newP1) )

            if self.isValidMove(oldP,newP2,False):
                allMoves.append( ((i,j),newP2) )

            if self.isValidMove(oldP,newP3,True):
                allMoves.append( ((i,j),newP3) )

        return allMoves


    def isValidMove(self,oldP,newP,vertical):
        (i,j) = newP
        isInBound = i<BOARD_SHAPE[0] and i>=0 and j<BOARD_SHAPE[1] and j>=0

        if isInBound:

            # if vertical new p can't have piece
            if vertical:
                return (self.board[newP] is None)

            # diagonal case, no capture or eat opponent
            else:
                return self.board[newP] is None or \
                       (self.board[newP].owner is not self.board[oldP].owner )

        return False




    def print(self):
        print('\n-----------------------------------------')
        for row in self.board:
            print('| ',end='')
            for piece in row:
                if piece is not None:
                    print(piece.owner,end=' | ')
                else:
                    print(' ',end = ' | ')
            print('\n-----------------------------------------')

        print("player 0:"+str(len(self.player0)))
        print([worker.position  for worker in self.player0])
        print("player 1:"+str(len(self.player1)))
        print([worker.position for worker in self.player1])


    # move do not have to check constraint! (handle by algorithm)
    def move(self,oldPosition,newPosition):
        # remove captured piece from player list
        (i,j) = newPosition
        newPosition = (i,j)
        (i, j) = oldPosition
        oldPosition = (i, j)

        captured = self.board[newPosition]
        if captured is not None:
            if captured.owner is 0:
                self.player0.remove(captured)
            else:
                self.player1.remove(captured)

        # update board state
        self.board[oldPosition].position = newPosition
        self.board[newPosition] = self.board[oldPosition]
        self.board[oldPosition] = None


    def checkWinner(self):
        if len(self.player0) is 0:
            return 1
        if len(self.player1) is 0:
            return 0

        for base in [piece.owner for piece in self.board[0] if piece is not None ]:
            if (base==1):
                return 1
        for base in [piece.owner for piece in self.board[4] if piece is not None]:
            if (base==0):
                return 0
        # there is no winner
        return -1
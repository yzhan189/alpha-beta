from Worker import Worker
from Player import Player
import numpy as np


class Board:

    def __init__(self,new=True):

        self.board = np.empty((8,8),dtype = object)
        self.player0 = list()
        self.player1 = list()
        if new:
            for j in range(8):
                # player0
                for i in [0, 1]:
                    self.board[(i,j)] = Worker((i,j),0)
                    self.player0.append(self.board[(i,j)])
                # player1
                for i in [6,7]:
                    self.board[(i,j)] = Worker((i,j),1)
                    self.player1.append(self.board[(i, j)])

    def copyMove(self,oldP,newP):
        copy = Board(False)
        for i in range(8):
            for j in range(8):
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
            (i,j) = worker.position
            newP1 = (i+direction,j+1)
            newP2 = (i+direction,j-1)
            newP3 = (i+direction,j)

            if self.isValidMove(newP1,False):
                allMoves.append( ((i,j),newP1) )

            if self.isValidMove(newP2,False):
                allMoves.append( ((i,j),newP2) )

            if self.isValidMove(newP3,True):
                allMoves.append( ((i,j),newP3) )

        return allMoves


    def isValidMove(self,newP,vertical):
        (i,j) = newP
        isValid = i<8 and i>=0 and j<8 and j>=0
        if not vertical:
            return isValid
        else:
            return isValid and self.board[newP] is None



    def print(self):
        print('\n---------------------------------')
        for row in self.board:
            print('| ',end='')
            for piece in row:
                if piece is not None:
                    print(piece.owner,end=' | ')
                else:
                    print(' ',end = ' | ')
            print('\n---------------------------------')

        print("player 0:"+str(len(self.player0)))
        print([worker.position  for worker in self.player0])
        print("player 1:"+str(len(self.player1)))
        print([worker.position for worker in self.player1])


    # move do not have to check constraint! (handle by algorithm)
    def move(self,oldPosition,newPosition):
        # remove captured piece from player list
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
        for base in [piece.owner for piece in self.board[7] if piece is not None]:
            if (base==0):
                return 0
        # there is no winner
        return -1
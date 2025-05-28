from enums.Colors import Color
from board.Position import Position
from abc import ABC, abstractmethod

class Piece(ABC):

    def __init__(self, color : Color, x, y):
        self.color = color
        self.pos = Position(y, x)
        
    def __str__(self):
        pass
    
    def getColor(self):
        return self.color

    def getPos(self):
        return self.pos
    
    def getInfo(self):
        return 'Color: ' + self.getColor().name + ', Position: ' + self.getPos().getPosName()
    
    def setMoves(self, moves):
        self.moves = moves

    def setPos(self, pos):
        self.pos = pos

    def setColor(self, color : Color):
        self.color = color

    def isValidMove(self, pos):
        v,h = Position.convertPos(pos)

        for i in self.moves:
            if Position(v, h).getPosName() == i.getPosName():
                return True
        return False

    @abstractmethod
    def initSquaresToMove(self):
        pass
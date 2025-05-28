from pieces.Piece import Piece
from enums.Colors import Color
class Empty(Piece):
    def __init__(self, color : Color, x, y):
        super().__init__(color, x, y)
        self.moveSquares = []
        super().setMoves(self.moveSquares)
    def __str__(self):
        return '█'
        
    def initSquaresToMove(self):
        return super().initSquaresToMove()

    def getInfo(self):
        return 'Empty ' + super().getInfo()
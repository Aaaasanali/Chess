from enums.Colors import Color
from pieces.Piece import Piece
class Player:
    def __init__(self, color : Color):
        self.pieces : list[Piece] = []
        self.color = color
        self.isChecked = False

    def addPiece(self, p : Piece):
        self.pieces.append(p)

    def getPieces(self):
        return self.pieces
    
    def reinitAllPieces(self):
        for i in self.pieces:
            i.initSquaresToMove()
    
    def removePiece(self, p: Piece):
        self.pieces.remove(p)
        return p
    
    def setCheck(self, b:bool):
        self.isChecked = b

    def getColor(self):
        return self.color
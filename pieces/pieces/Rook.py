from pieces.Piece import Piece
from enums.Colors import Color
from players.White import White
from players.Black import Black
from board.Position import Position

class Rook(Piece):
    def __init__(self, color : Color, x, y):
        super().__init__(color, x, y)
        self.moveSquares = []
        self.moveSquares = self.initSquaresToMove()

    def __str__(self):
        return '♜'
    
    def initSquaresToMove(self):
            moves = []
            current_position : Position = super().getPos()
            v = current_position.getV()
            h = current_position.getH()

            found = False
            for i in range(v+1, 8):
                for j in White().getPieces() + Black().getPieces():
                    if(Position(i, h).getPosName() == j.getPos().getPosName() and self != j):
                        found = True
                        if self.getColor() == j.getColor().opposite:
                            moves.append(Position(i, h))
                        break
                if found: 
                    break
                moves.append(Position(i, h))
            found = False
            for i in range(v-1, -1, -1):
                for j in White().getPieces() + Black().getPieces():
                    if(Position(i, h).getPosName() == j.getPos().getPosName() and self != j):
                        found = True
                        if self.getColor() == j.getColor().opposite:
                            moves.append(Position(i, h))
                        break
                if found: 
                    break
                moves.append(Position(i, h))
            found = False
            for i in range(h+1, 8):
                for j in White().getPieces() + Black().getPieces():
                    if(Position(v, i).getPosName() == j.getPos().getPosName() and self != j):
                        found = True
                        if self.getColor() == j.getColor().opposite:
                            moves.append(Position(v, i))
                        break
                if found: 
                    break
                moves.append(Position(v, i))
            found = False
            for i in range(h-1, -1, -1):
                for j in White().getPieces() + Black().getPieces():
                    if(Position(v, i).getPosName() == j.getPos().getPosName() and self != j):
                        found = True
                        if self.getColor() == j.getColor().opposite:
                            moves.append(Position(v, i))
                        break
                if found: 
                    break
                moves.append(Position(v, i))
            
            super().setMoves(moves)

    def getInfo(self):
        return 'Rook, ' + super().getInfo()
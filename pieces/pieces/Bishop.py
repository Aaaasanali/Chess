from pieces.Piece import Piece
from enums.Colors import Color
from players.White import White
from players.Black import Black
from board.Position import Position

class Bishop(Piece):
    def __init__(self, color : Color, x, y):
        super().__init__(color, x, y)
        self.moveSquares = []
        self.moveSquares = self.initSquaresToMove()
    def __str__(self):
        return  '♗'
    
    def initSquaresToMove(self):
            moves = []
            directions = [(-1, -1), (-1, +1), (+1, -1), (+1, +1)]
            current_position : Position = super().getPos()
            v = current_position.getV()
            h = current_position.getH()

            found = False
            k = 0
            for dx, dy in directions:
                x, y = v + dx, h + dy
                while 0 <= x < 8 and 0 <= y < 8:
                    pos = Position(x, y)
                    found = False
                    for piece in White().getPieces() + Black().getPieces():
                        if pos.getPosName() == piece.getPos().getPosName() and self != piece:
                            found = True
                            if self.getColor() == piece.getColor().opposite:
                                moves.append(pos)  # Can capture enemy
                            break
                    if found:
                        break
                    moves.append(pos)  # Empty square
                    x += dx
                    y += dy
            
            super().setMoves(moves)

    def getInfo(self):
        return 'Bishop, ' + super().getInfo()
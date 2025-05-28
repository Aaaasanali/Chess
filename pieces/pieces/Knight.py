from pieces.Piece import Piece
from enums.Colors import Color
from board.Position import Position
from players.White import White
from players.Black import Black
class Knight(Piece):
    def __init__(self, color : Color, x, y):
        super().__init__(color, x, y)
        self.moveSquares = []
        self.moveSquares = self.initSquaresToMove()
    def __str__(self):
        return '♞'
    
    def initSquaresToMove(self):
            moves = []
            directions = [
                (-2, -1), (-2, +1),
                (-1, -2), (-1, +2),
                (+1, -2), (+1, +2),
                (+2, -1), (+2, +1),
            ]

            current_position : Position = super().getPos()

            v = current_position.getV()
            h = current_position.getH()
            
            moves = []
            for dr, dc in directions:
                hor, vert = h + dr, v + dc
                if 0 <= hor < 8 and 0 <= vert < 8:
                    found = False
                    for j in White().getPieces() + Black().getPieces():
                        if(Position(vert, hor).getPosName() == j.getPos().getPosName() and self != j):
                            found = True
                            if self.getColor() == j.getColor().opposite:
                                moves.append(Position(vert, hor))
                                break
                    if found:
                        continue
                    moves.append(Position(vert, hor))
            super().setMoves(moves)
    
    def getInfo(self):
        return 'Knight, ' + super().getInfo()
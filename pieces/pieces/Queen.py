from pieces.Piece import Piece
from enums.Colors import Color
from players.White import White
from players.Black import Black
from board.Position import Position
class Queen(Piece):
    def __init__(self, color : Color, x, y):
        super().__init__(color, x, y)
        self.moveSquares = []
        self.moveSquares = self.initSquaresToMove()
    def __str__(self):
        return  '♕'
    
    def initSquaresToMove(self):
            moves = []
            directions = [
                (-1, 0), (1, 0), (0, -1), (0, 1),      # Rook directions
                (-1, -1), (-1, 1), (1, -1), (1, 1)     # Bishop directions
            ]

            current_position : Position = super().getPos()
            v = current_position.getV()
            h = current_position.getH()
            for dx, dy in directions:
                x, y = v + dx, h + dy
                while 0 <= x < 8 and 0 <= y < 8:
                    pos = Position(x, y)
                    found = False
                    for piece in White().getPieces() + Black().getPieces():
                        if pos.getPosName() == piece.getPos().getPosName() and self != piece:
                            found = True
                            if self.getColor() == piece.getColor().opposite:
                                moves.append(pos)  # Capture
                            break
                    if found:
                        break
                    moves.append(pos)
                    x += dx
                    y += dy
            super().setMoves(moves)


    def getInfo(self):
        return 'Queen, ' + super().getInfo()
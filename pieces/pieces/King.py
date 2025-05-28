from pieces.Piece import Piece
from enums.Colors import Color
from players.White import White
from players.Black import Black
from board.Position import Position
class King(Piece):
    def __init__(self, color : Color, x, y):
        super().__init__(color, x, y)
        self.moveSquares = []
        self.moveSquares = self.initSquaresToMove()
        self.checked = False
        self.player = White() if super().getColor() == Color.WHITE else Black()

    def __str__(self):
        return '♔'
    def initSquaresToMove(self):
            
            directions = [
                (-1, 0), (1, 0), (0, -1), (0, 1),      # Rook directions
                (-1, -1), (-1, 1), (1, -1), (1, 1)     # Bishop directions
            ]

            current_position : Position = super().getPos()
            v = current_position.getV()
            h = current_position.getH()
            opposite = (super().getColor() == Color.WHITE) if Black() else White()
            
            moves = []
            for dx, dy in directions:
                x, y = v + dx, h + dy
                if 0 <= x < 8 and 0 <= y < 8:
                    pos = Position(x, y)
                    found = False
                    for piece in White().getPieces() + Black().getPieces():
                        if pos.getPosName() == piece.getPos().getPosName() and self != piece:
                            found = True
                            if self.getColor() == piece.getColor().opposite:
                                moves.append(pos)  # Capture
                            break
                    if found:
                        continue
                    moves.append(pos)
            super().setMoves(moves) 
    
    def isOnCheck(self):
        current_position : Position = super().getPos()
        opposite = Black() if (super().getColor() == Color.WHITE) else White()
        for piece in opposite.pieces:
            for dsq in piece.moves:
                    if current_position.getPosName() == dsq.getPosName():
                        self.checked = True
                        self.player.setCheck(True)
                        return self.checked
        self.checked = False
        self.player.setCheck(False)
        return self.checked

    def isValidMove(self, pos):
        v,h = Position.convertPos(pos)
        opposite = Black() if (super().getColor() == Color.WHITE) else White()
        for piece in opposite.pieces:
                for dsq in piece.moves:
                    if Position(v,h).getPosName() == dsq.getPosName():
                        return False
        for i in self.moves:
            if Position(v, h).getPosName() == i.getPosName():
                return True
        return False
    
    def getInfo(self):
        return 'King, ' + super().getInfo()
from pieces.Piece import Piece
from enums.Colors import Color
from players.White import White
from players.Black import Black
from board.Position import Position
class Pawn(Piece):
    def __init__(self, color : Color, x, y):
        super().__init__(color, x, y)
        self.firstMove = False
        self.initPos = super().getPos()
        self.moveSquares = []
        self.moveSquares = self.initSquaresToMove()
        

    def __str__(self):
        return '♙'
    
    def initSquaresToMove(self):
        moves = []
        current_position : Position = super().getPos()
        if current_position.getPosName() != self.initPos.getPosName():
            self.firstMove = True
        v = current_position.getV()
        h = current_position.getH()

        if super().getColor() == Color.BLACK:
                pos1, pos2 = Position(v, h-1), Position(v, h-2)
        else:
            pos1, pos2 = Position(v, h+1), Position(v, h+2)
        found1, found2 = False, False
        if not self.firstMove:
            for piece in White().getPieces() + Black().getPieces():
                if pos1.getPosName() == piece.getPos().getPosName() and self != piece:
                    found1 = True
                    break
                if pos2.getPosName() == piece.getPos().getPosName() and self != piece:
                    found2 = True
            if not found1:
                moves.append(pos1)
            if not found2 and not found1:
                moves.append(pos2)
        else:
            for piece in White().getPieces() + Black().getPieces():
                if pos1.getPosName() == piece.getPos().getPosName() and self != piece:
                    found1 = True
                    break
            if not found1:
                moves.append(pos1)
        
        if super().getColor() == Color.BLACK:
            pos3, pos4 = Position(v-1, h-1), Position(v+1, h-1)
        else:
            pos3, pos4 = Position(v-1, h+1), Position(v+1, h+1)

        for piece in White().getPieces() + Black().getPieces():
            if pos3.getPosName() == piece.getPos().getPosName() and self != piece and self.getColor() == piece.getColor().opposite:
                pos3.setPawnDangerPos()
                moves.append(pos3)
            if pos4.getPosName() == piece.getPos().getPosName() and self != piece and self.getColor() == piece.getColor().opposite:
                pos4.setPawnDangerPos()
                moves.append(pos4)
        super().setMoves(moves)

    def getInfo(self):
        return 'Pawn, ' + super().getInfo()
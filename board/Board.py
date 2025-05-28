from enums.Colors import Color

from pieces.pieces.Empty import Empty
from pieces.pieces.Pawn import Pawn
from pieces.pieces.Rook import Rook
from pieces.pieces.Queen import Queen
from pieces.pieces.Knight import Knight
from pieces.pieces.Bishop import Bishop
from pieces.pieces.King import King


from board.Position import Position
from pieces.Piece import Piece

from players.White import White
from players.Black import Black
from players.Player import Player

from board.Square import Square

from rich import print

class Board:

    board = [[Square(Empty(Color.WHITE, i, j)) for j in range(8)] for i in range(8)]
    def __init__(self):
        self.generateEmptyBoard()

        for i in range (8): # Pawns generator
            Board.setPiece(Pawn(Color.WHITE, 1, i), 1, i)
            Board.setPiece(Pawn(Color.BLACK, 6, i), 6, i)
        Board.setPiece(Rook(Color.WHITE, 0, 0), 0, 0) # Rooks generator
        Board.setPiece(Rook(Color.WHITE, 0, 7), 0, 7)
        Board.setPiece(Rook(Color.BLACK, 7, 0), 7, 0)
        Board.setPiece(Rook(Color.BLACK, 7, 7), 7, 7)

        Board.setPiece(Knight(Color.WHITE, 0, 1), 0, 1) # Knights generator
        Board.setPiece(Knight(Color.WHITE, 0, 6), 0, 6)
        Board.setPiece(Knight(Color.BLACK, 7, 1), 7, 1)
        Board.setPiece(Knight(Color.BLACK, 7, 6), 7, 6)

        Board.setPiece(Bishop(Color.WHITE, 0, 2), 0, 2) # Bishops generator
        Board.setPiece(Bishop(Color.WHITE, 0, 5), 0, 5)
        Board.setPiece(Bishop(Color.BLACK, 7, 2), 7, 2) 
        Board.setPiece(Bishop(Color.BLACK, 7, 5), 7, 5)

        Board.setPiece(King(Color.WHITE, 0, 4), 0, 4) # Kings generator
        Board.setPiece(King(Color.BLACK, 7, 4), 7, 4)

        Board.setPiece(Queen(Color.WHITE, 0, 3), 0, 3) # Queens generator
        Board.setPiece(Queen(Color.BLACK, 7, 3), 7, 3)
            

    def generateEmptyBoard(self):
        for i in range(8):
            for j in range(0, 8, 2):
                if(i%2 == 0):
                    Board.board[i][j] = Square(Empty(Color.BLACK, i, j))
                    Board.board[i][j].setColor(Color.BLACK)
                    Board.board[i][j+1] = Square(Empty(Color.WHITE, i, j+1))
                    Board.board[i][j+1].setColor(Color.WHITE)
                else:
                    Board.board[i][j] = Square(Empty(Color.WHITE, i, j))
                    Board.board[i][j].setColor(Color.WHITE)
                    Board.board[i][j+1] = Square(Empty(Color.BLACK, i, j+1))
                    Board.board[i][j+1].setColor(Color.BLACK)

    def getBoard(self):
        for p in White().getPieces() + Black().getPieces():
            if isinstance(p, Pawn):
                for m in p.moves:
                    if m.isPawnDangerPos():
                        sq = self.getSquare(m)
                        if isinstance(sq.getCont(), Empty) or sq.getCont().color == p.getColor().opposite:
                            sq.setDanger(p.getColor(), p)
            else:
                for m in p.moves:
                    sq = self.getSquare(m)
                    if isinstance(sq.getCont(), Empty) or sq.getCont().color == p.getColor().opposite:
                        sq.setDanger(p.getColor(), p)
        

        res = ''
        res += "  a b c d e f g h\n"
        for i in range (7, -1, -1):
            res += str(i+1) + ' '
            for j in range (8):
                res += self.board[i][j].__str__()
                if isinstance(self.board[i][j], Piece) and not isinstance(self.board[i][j], Empty):
                    res += ' '
            res += '\n'
        return res
    
    def __setPick(self, sq : Square):
        self.pick = sq
        self.pick.setPick(True)

    def getPickedPiece(self):
        return self.pick

    def resetDangerSquares(self):
        for i in White().getPieces() + Black().getPieces():
            for j in i.moves:
                self.getSquare(j).setDanger(Color.EMPTY, i)


    def __movingAlgorithm(self, pos, piece:Piece, mateChecking:bool = False):
        self.resetDangerSquares()
        v,h = Position.convertPos(pos)
        newPos = Position(v, h)
        newSquare = self.getSquare(newPos)
        initialSquare = self.getSquare(piece.getPos())
        initialPos = piece.getPos()
        removedPiece = newSquare.getCont()

        player = White() if piece.getColor() == Color.WHITE else Black()
        opponent = Black() if piece.getColor() == Color.WHITE else White()

        plKing : King=None
        for i in player.getPieces():
            if isinstance(i, King):
                plKing = i
        oppKing : King=None
        for i in opponent.getPieces():
            if isinstance(i, King):
                oppKing = i

        capturing = False
        if newSquare.isBusy() and newSquare.getCont().getColor() != piece.getColor():
            capturing = True
            opponent.removePiece(removedPiece)
        
        newSquare.setCont(piece)
        initialSquare.emptyCont(piece.getPos())
        piece.setPos(newPos)
        
        if isinstance(piece, Pawn) and h==7:
            self.promotePawn(self.getSquare(Position(v, h)), piece)

        White().reinitAllPieces()
        Black().reinitAllPieces()

        if plKing.isOnCheck() or mateChecking:
            wasCheck = plKing.isOnCheck()
            self.resetDangerSquares()
            if capturing:
                opponent.addPiece(removedPiece)
            newSquare.setCont(removedPiece)
            
            initialSquare.setCont(piece)
            piece.setPos(initialPos)

            White().reinitAllPieces()
            Black().reinitAllPieces()

            if mateChecking:
                if wasCheck:
                    return True
                return False

            return False
        if oppKing.isOnCheck() and self.isMate(opponent):
            print('Mate!', player.getColor().name, 'Won!')
            self.pick.setPick(False)
            print(self.getBoard())
            exit()
        if plKing.isOnCheck() and self.isMate(player):
            print('Mate!', opponent.getColor().name, 'Won!')  
            self.pick.setPick(False)
            print(self.getBoard())
            exit()          
        return True

    def isMate(self, pl:Player):
        for p in pl.getPieces():
            for m in p.moves:
                if not self.__movingAlgorithm(m.getPosName(), p, mateChecking=True):
                    return False
        return True


    def movePiece(self, pos):
        if self.pick.getCont().isValidMove(pos):
            if self.__movingAlgorithm(pos, self.getPickedPiece().getCont()):
                self.pick.setPick(False)
                return True
        return False

    def promotePawn(self, sq:Square, p:Piece):
        v,h = p.getPos().getV(), p.getPos().getH()
        newPiece : Piece = None
        while(True):
            print('Pick a piece:')
            print('0 - ♕')
            print('1 - ♖')
            print('2 - ♗')
            print('3 - ♘')
            match int(input()):
                case 0:
                    newPiece = Queen(p.getColor(), h, v)
                    break
                case 1:
                    newPiece = Rook(p.getColor(), h, v)
                    break
                case 2:
                    newPiece = Bishop(p.getColor(), h, v)
                    break
                case 3:
                    newPiece = Knight(p.getColor(), h, v)
                    break
                case _:
                    continue
        sq.setCont(newPiece)
        if(p.getColor() == Color.WHITE):
            White().removePiece(p)
            White().addPiece(newPiece)
        else:
            Black().removePiece(p)
            Black().addPiece(newPiece)
        return

    def setPiece(p : Piece, x, y):
        Board.board[x][y].setCont(p)
        if p.getColor() == Color.WHITE:
            White().addPiece(p)
        else:
            Black().addPiece(p)
        White().reinitAllPieces()

    def getPiece(self, pick, color:Color):
        x = ord(pick[0])-96
        y = pick[1]
        if isinstance(self.board[int(y)-1][x-1].getCont(), Empty):
            return False
        elif self.board[int(y)-1][x-1].getCont().getColor() == color:
            self.__setPick(self.board[int(y)-1][x-1])
            return True
        return False
        
    def getSquare(self, pos : Position):
        return Board.board[pos.getH()][pos.getV()]
    
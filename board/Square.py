from pieces.Piece import Piece
from enums.Colors import Color

from pieces.pieces.Empty import Empty

class Square:
    def __init__(self, piece : Piece):
        self.container = piece
        self.color:Color = Color.BLACK
        self.danger:Color = Color.EMPTY
        self.picked = False
        self.isChecked = False

    def setColor(self, color : Color):
        self.color = color

    def setCont(self, piece : Piece):
        self.container = piece
    def getCont(self):
        return self.container

    def setDanger(self, d:Color, p:Piece):
        if d == Color.BLACK or d == Color.WHITE:
            if self.danger == d.opposite:
                self.danger = Color.GREEN
            elif self.danger == Color.GREEN:
                pass
            else:
                self.danger = d
        if d == Color.EMPTY:
            if self.danger == Color.GREEN:
                self.danger = p.getColor().opposite
            elif self.danger == Color.BLACK or self.danger == Color.WHITE:
                self.danger = d
                

    def isDanger(self):
        return self.danger

    def setPick(self, b):
        self.picked = b
    def isPicked(self):
        return self.picked

    def emptyCont(self, pos):
        self.container = Empty(self.color, pos.getV(), pos.getH())

    def getInfo(self):
        return self.container.getInfo()

    def isBusy(self):
        return False if isinstance(self.container, Empty) else True



    def __str__(self):

        if self.picked:
            if self.container.getColor() == Color.WHITE:
                return '[yellow on blue]' + self.container.__str__() + ' [/]'
            else:
                return '[red on blue]' + self.container.__str__() + ' [/]'
            
        if self.isChecked:
            if self.container.getColor() == Color.WHITE:
                return '[yellow on purple]' + self.container.__str__() + ' [/]'
            else:
                return '[red on purple]' + self.container.__str__() + ' [/]'

        # if self.danger != Color.EMPTY:
        #     if isinstance(self.container, Empty):
        #         if self.danger == Color.WHITE:
        #             return '[yellow on yellow]' + self.container.__str__() + ' [/]'
        #         elif self.danger == Color.BLACK:
        #             return '[red on red]' + self.container.__str__() + ' [/]'
        #         elif self.danger == Color.GREEN:
        #             return '[green on green]' + self.container.__str__() + ' [/]'
        
        #     if self.container.getColor() == Color.WHITE and self.danger == Color.WHITE:
        #         return '[yellow on yellow]' + self.container.__str__() + ' [/]'
        #     elif self.container.getColor() == Color.WHITE and self.danger == Color.BLACK:
        #         return '[yellow on red]' + self.container.__str__() + ' [/]'
        #     elif self.container.getColor() == Color.BLACK and self.danger == Color.WHITE:
        #         return '[red on yellow]' + self.container.__str__() + ' [/]'
        #     elif self.container.getColor() == Color.BLACK and self.danger == Color.BLACK:
        #         return '[red on red]' + self.container.__str__() + ' [/]'


        if isinstance(self.container, Empty):
            if self.color == Color.WHITE:
                return '[white on white]' + self.container.__str__() + ' [/]'
            else:
                return '[black on black]' + self.container.__str__() + ' [/]'
        
        if self.container.getColor() == Color.WHITE and self.color == Color.WHITE:
            return '[yellow on white]' + self.container.__str__() + ' [/]'
        elif self.container.getColor() == Color.WHITE and self.color == Color.BLACK:
            return '[yellow on black]' + self.container.__str__() + ' [/]'
        elif self.container.getColor() == Color.BLACK and self.color == Color.WHITE:
            return '[red on white]' + self.container.__str__() + ' [/]'
        else:
            return '[red on black]' + self.container.__str__() + ' [/]'
        
    
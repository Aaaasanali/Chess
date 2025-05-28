from enums.Colors import Color
from board.Board import Board
from players.Black import Black
from players.White import White
from rich import print
br = Board()

wh = White()
bl = Black()

run = True
while run:
    print(br.getBoard())
    while True:
        print("Whites Turn")
        piecePick = input()
        try:
            if br.getPiece(piecePick, Color.WHITE):
                break
            else:
                print("Not Your Piece")
                continue
        except IndexError:
            print('Not Valid... Idiot')
            
    print(br.getBoard())
    while True:
        pos = input()
        try:
            if br.movePiece(pos):
                print("Yeah you can move there")
                break
            else:
                print("Nah, Not valid")
                continue
        except IndexError:
            print('Not Valid... Idiot')
        
    print(br.getBoard())
    while True:
        print('White Checked: ', wh.isChecked, 'Black Checked: ', bl.isChecked)
        print("Blacks Turn")
        piecePick = input()
        try:
            if br.getPiece(piecePick, Color.BLACK):
                break
            else:
                print("Not Your Piece")
                continue
        except IndexError:
            print('Not Valid... Idiot')
            
    print(br.getBoard())
    while True:
        pos = input()
        try:
            if br.movePiece(pos):
                print("Yeah you can move there")
                break
            else:
                print("Nah, Not valid")
                continue
        except IndexError:
            print('Not Valid... Idiot')
    
    
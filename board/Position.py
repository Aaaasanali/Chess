
class Position:
    def __init__(self, vertical, horizontal):
        self.vert : int = vertical
        self.hor : int = horizontal
        self.pawnDangerPos = False

    def getPosName(self):
        return str(chr(self.vert+97)) +  str(self.hor+1)
    
    def setPawnDangerPos(self):
        self.pawnDangerPos = True
    def isPawnDangerPos(self):
        return self.pawnDangerPos

    def getPos(self):
        return str(self.vert) + str(self.hor)
    
    def getV(self):
        return self.vert
    
    def getH(self):
        return self.hor
    
    @staticmethod
    def convertPos(pos):
        v = pos[0]
        h = pos[1]
        return (ord(v)-97, int(h)-1)
from enum import Enum

class Color(Enum):
    BLACK = 0
    WHITE = 1
    YELLOW = 2
    RED = 3
    GREEN = 4
    EMPTY = -1

    @property
    def opposite(self):
        return Color.BLACK if self == Color.WHITE else Color.WHITE
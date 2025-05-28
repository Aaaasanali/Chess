from .Player import Player
from enums.Colors import Color

class Black(Player):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._initialized = False
        return cls._instance

    def __init__(self):
        if not getattr(self, '_initialized', False):
            super().__init__(Color.BLACK)
            self._initialized = True
from enums import Color, Kind
from Piece import Piece


class Player:
    color: Color = None
    name: str
    score: int = 0
    pieces: list[Piece]

    def __init__(self, name: str):
        self.name = name





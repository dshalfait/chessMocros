from enum import Enum


class Color(Enum):
    BLACK = "B"
    WHITE = "W"
    EMPTY = "-"


class Kind(Enum):
    KING = "K"
    QUEEN = "Q"
    BISHOP = "B"
    KNIGHT = "N"
    ROOK = "R"
    EMPTY = "-"

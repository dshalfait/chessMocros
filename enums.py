from enum import Enum, IntEnum, EnumMeta


class MetaEnum(EnumMeta):
    def __contains__(cls, item):
        try:
            cls(item)
        except ValueError:
            return False
        return True


class Color(Enum, metaclass=MetaEnum):
    BLACK = "B"
    WHITE = "W"
    EMPTY = "-"


class Kind(Enum, metaclass=MetaEnum):
    KING = "K"
    QUEEN = "Q"
    BISHOP = "B"
    KNIGHT = "N"
    ROOK = "R"
    PAWN = "P"
    EMPTY = "-"


class Rows(IntEnum, metaclass=MetaEnum):
    ONE = 0
    TWO = 1
    THREE = 2
    FOUR = 3
    FIVE = 4
    SIX = 5
    SEVEN = 6
    EIGHT = 7


class Cols(IntEnum, metaclass=MetaEnum):
    A = 0
    B = 1
    C = 2
    D = 3
    E = 4
    F = 5
    G = 6
    H = 7

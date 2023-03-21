from enums import Kind, Color
from Move import Move



class Piece:
    kind: Kind
    color: Color
    poss_moves: list[Move] | None = None

    def __init__(self, color: Color = Color.EMPTY, kind: Kind = Kind.EMPTY, ):
        self.color = color
        self.kind = kind




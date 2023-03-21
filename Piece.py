from enums import Kind
from Move import Move


class Piece:
    kind: Kind
    poss_moves: list[Move]

from Piece import Piece
from enums import Color, Kind, Rows, Cols


class Board:
    def __init__(self):
        self.field = [[Piece() for col in range(len(Cols))] for row in range(len(Rows))]
        self.board_init()

    def init_first_last_row(self, row: Rows):
        if not (row == 0 or row == 7):
            raise ValueError

        if row == 0:
            color = Color.WHITE
        else:
            color = Color.BLACK

        self.field[row][Cols.A] = Piece(color, Kind.ROOK)
        self.field[row][Cols.B] = Piece(color, Kind.KNIGHT)
        self.field[row][Cols.C] = Piece(color, Kind.BISHOP)
        self.field[row][Cols.D] = Piece(color, Kind.QUEEN)
        self.field[row][Cols.E] = Piece(color, Kind.KING)
        self.field[row][Cols.F] = Piece(color, Kind.BISHOP)
        self.field[row][Cols.G] = Piece(color, Kind.KNIGHT)
        self.field[row][Cols.H] = Piece(color, Kind.ROOK)

    def init_pawn_row(self, row: int):
        if not (row == 1 or row == 6):
            raise ValueError
        if row == 1:
            color = Color.WHITE
        else:
            color = Color.BLACK
        self.field[row] = [Piece(color, Kind.PAWN) for i in range(len(Cols))]
    def board_init(self):
        # Initialize

        self.init_first_last_row(Rows.ONE)
        self.init_first_last_row(Rows.EIGHT)

        self.init_pawn_row(Rows.TWO)
        self.init_pawn_row(Rows.SEVEN)
    def plot(self, color: Color = Color.BLACK):
        col_list_letter = [(list(Cols)[i]).name for i in range(len(Cols))]
        row_list = list(reversed(range(len(Rows))))
        col_list = list(range(len(Cols)))

        if color == Color.BLACK:
            col_list_letter = reversed(col_list_letter)
            row_list = list(reversed(row_list))
            col_list = list(reversed(col_list))

        string = "    {0}  {1}  {2}  {3}  {4}  {5}  {6}  {7}\n".format(*col_list_letter)
        string += "    -----------------------\n"
        for x in row_list:
            string += str(x + 1) + " | "
            for y in col_list:
                piece: Piece = self.field[x][y]
                string += piece.color.value + piece.kind.value + " "
            string += "\n"
        print(string)



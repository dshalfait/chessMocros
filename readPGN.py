from builtins import len, ValueError

from Move import Move
from enums import Kind, Color, Cols, Rows


class readPGN:
    def __init__(self, filename="Adams.pgn"):
        self.file_r = open(filename, "r").read()

    def read_game(self, game_no=1):
        return self.file_r.split("\n\n")[(game_no - 1) * 2 + 1]

    def clean_moves(self, moves: str):
        replace_list = ['x', '1-0', '+', '\n']
        clean_mvs: str = moves
        for chars in replace_list:
            if chars == '\n':
                clean_mvs = clean_mvs.replace(chars, ' ')
                continue
            clean_mvs = clean_mvs.replace(chars, '')
        return clean_mvs

    def moves_to_list(self, clean_moves: str):
        cl_mv_dot = clean_moves.split('.')
        cl_mv_dot.pop(0)
        moves_p1 = []
        moves_p2 = []
        cl_mv_dot[len(cl_mv_dot) - 1] = cl_mv_dot[len(cl_mv_dot) - 1].strip()  # .strip() necessary for last move only
        for i in range(0, len(cl_mv_dot)):
            mv_split_by_player = cl_mv_dot[i].split(' ')
            moves_p1.append(mv_split_by_player[0])
            if len(mv_split_by_player) < 2:
                continue
            moves_p2.append(mv_split_by_player[1])
        return moves_p1, moves_p2

    def pawn_move(self, move: str):
        move_copy = move
        match len(move_copy):
            case 2:
                col = move_copy[0]
                row = move_copy[1]
                if not col.isalpha() or not row.isnumeric():
                    ValueError('you mixed the order, first a col(column) than a row(row)')
                return Move(col, int(row))  # Pawn move
            case 3:
                prev_pos = move_copy[0]
                col = move_copy[1]
                row = move_copy[2]
                if not col.isalpha() or not row.isnumeric():
                    ValueError('you mixed the order! Correct Notation is [prev_col][col][row]')
                return Move(col, int(row), prev_pos=prev_pos)

    def castling(self, player: str, side: str):
        if player == 'W':
            king = Kind.KING.value
            rook = Kind.ROOK.value
            k_row = r_row = 1
            if side == 'k':
                k_col = Cols.G.name
                r_col = Cols.F.name  # only for castling return two moves one for king one for rrok
            else:
                k_col = Cols.C.name
                r_col = Cols.D.name
        else:
            k_row = r_row = 8
            if player == 'k':
                k_col = Cols.G.name
                r_col = Cols.F.name # only for castling return two moves one for king one for rrok
            else:
                k_col = Cols.C.name
                r_col = Cols.D.name  # only for castling return two moves one for king one for rook

        return Move(k_col, k_row, king), Move(r_col, r_row, rook)

    def three_letters_move(self, move: str, player: str):
        kind = move[0]
        col = move[1]
        row = move[2]

        # Error Handling should be professionalized
        if kind in Kind:
            return Move(col, int(row), kind)
        elif move[0] == 'O':
            return self.castling(player, side = 'k')
        else:
            if not col.isalpha() or not row.isnumeric() or not kind.isalpha():
                raise ValueError('Invalid Move: you mixed the order, correct order is [kind][col][row] or castling wrong notation')


    def four_letters_move(self, move: str):
        kind = move[0]
        prev_pos = move[1]
        col = move[2]
        row = move[3]

        if not col.isalpha() or not row.isnumeric() or not kind.isalpha():
            raise ValueError('you mixed the order, correct order is [kind][prev_col][col][row]')

        return Move(col, int(row), kind, prev_pos)

    def five_letters_move(self, move: str, player: str):
        if move == "O-O-O":
            return self.castling(player, side='q')

    def read_move(self, move: str, player: str):
        if len(move) < 2:
            raise ValueError('a move with less than 2 chars is input, but can not be interpreted, please fix that')

        # Pawn move
        if move[0].islower():  # Pawn Move
            return self.pawn_move(move)
        else:
            match len(move):
                case 3:
                    return self.three_letters_move(move, player)
                case 4:
                    return self.four_letters_move(move)
                case 5:
                    return self.five_letters_move(move, player)


if __name__ == '__main__':
    rPGN: readPGN = readPGN()
    for i in range(3422):
        r_game: str = rPGN.read_game(i)
        clean_moves = rPGN.clean_moves(r_game)
        moves_p1, moves_p2 = rPGN.moves_to_list(clean_moves)
        for move in moves_p1:
            print(move)
            a = rPGN.read_move(move, "W")
        print(moves_p1)
    # print(str(a.kind) + str(a.row) + str(a.col))

from Player import Player
from Board import Board
from enums import Color, Kind, Cols, Rows
import random
import time


class Game:
    def __init__(self):
        self.turn: Player | None = None
        self.board: Board = Board()
        self.p1: Player = Player("Human")
        self.p2: Player = Player("CPU")

    def color_decision(self):
        print('Black or White? \nLet chance decide')

        if random.randint(0, 1):
            self.p1.color = Color.WHITE
            self.p2.color = Color.BLACK
        else:
            self.p2.color = Color.BLACK
            self.p1.color = Color.WHITE

        print("{}: {}; {}: {}".format(self.p1.name, self.p1.color.name, self.p2.name, self.p2.color.name))
        return self.p1 if self.p1.color == Color.WHITE else self.p2

    def swap_turn(self):
        return self.p1 if self.turn == self.p2 else self.p2

    @staticmethod
    def input_in_range(letter: str, number: str):
        number = int(number)
        if not (Cols.__contains__(letter) and Rows.__contains__(number - 1)):
            raise ValueError('Letter or Number not in permissible range')

        return True

    def move_procedure(self):
        print("{}'s Move:".format(self.turn.name))
        self.board.plot(self.turn.color)
        pieces_abbrev = ""
        for i in range(len(Kind) - 1):
            pieces_abbrev += "{}: {} | ".format(list(Kind)[i].name, list(Kind)[i].value)
        kind_to_move = input('{} \nEnter the piece you want to move: '.format(pieces_abbrev))

        if not Kind.__contains__(kind_to_move):
            raise ValueError('No such piece, use the mentioned abbreviations!')
        print('Letter: A - H + Number: 1 - 8')
        letter, number = list(
            map(str, input(
                'Enter the position you want to move to (Letter, Number): ').split()))
        try:
            self.input_in_range(letter, number)
        except ValueError as err:
            print(err)

        print(letter + number)

    def start(self):
        print("Hello mate, let's play chess!")

        checkmate = False
        self.turn: Player = self.color_decision()

        tic = time.perf_counter()

        while not checkmate:
            try:
                toc = time.perf_counter()
                if toc - tic > 10:
                    checkmate = True
                    print(toc - tic)

                self.move_procedure()

                self.turn = self.swap_turn()

            except ValueError as err:
                print(err)

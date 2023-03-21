from Player import Player
from Board import Board
import random


class Game:
    def __init__(self):
        self.board = Board()

    @staticmethod
    def color_decision(p1: Player, p2: Player):
        print('Black or White? \nLet chance decide')

        if random.randint(0, 1):
            p1.color = 'W'
            p2.color = 'B'
        else:
            p2.color = 'W'
            p1.color = 'B'

        print("Human: {}; CPU: {}".format(p1.color, p2.color))


    def start(self):
        print("Hello mate, let's play chess!")
        self.board.plot()

        human = Player()
        cpu = Player()

        self.color_decision(human, cpu)
from Player import Player
from Board import Board



class Game:


    def __init__(self):
        self.board = [['--' for col in range(Game.COLS)] for row in range(Game.ROWS)]

    def board_init(self):
        self.board[0] = ['WR', 'WN', 'WB', 'WQ', 'WK', 'WB', 'WN', 'WR']
        self.board[1] = ['WP'] * 8

        self.board[6] = ['BP'] * 8
        self.board[7] = ['BR', 'BN', 'BB', 'BQ', 'BK', 'BB', 'BN', 'BR']

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



    def plot_board(self, player=None):
        string = "    A  B  C  D  E  F  G  H\n"
        string += "    -----------------------\n"
        for x in range(Game.ROWS):
            string += str(x + 1) + " | "
            for y in range(Game.COLS):
                string += self.board[x][y] + " "
            string += "\n"
        print(string)

    def start(self):
        print("Hello mate, let's play chess!")
        self.board_init()
        self.plot_board()

        human = Player()
        cpu = Player()

        self.color_decision(human, cpu)
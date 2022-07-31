# Вся игра
# from random import randint
#
#
# class Cell:
#     def __init__(self, around_mines=0, mine=False):
#         self.around_mines = around_mines
#         self.mine = mine
#         self.fl_open = True
#
#
# class GamePole:
#     def __init__(self, N, M):
#         self.N = N
#         self.M = M
#         self.pole = [[Cell() for n in range(self.N)] for n in range(self.N)]
#         self.init()
#
#     def init(self):
#         for i in range(self.M):
#             random_1 = randint(0, self.N - 1)
#             random_2 = randint(0, self.N - 1)
#             if self.pole[random_1][random_2].mine:
#                 continue
#             self.pole[random_1][random_2] = Cell(mine=True)
#         around_the_cage = (-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)
#         for i in range(self.N):
#             for j in range(self.N):
#                 if not self.pole[i][j].mine:
#                     self.pole[i][j].around_mines = sum((self.pole[i + x][j + y].mine for x, y in around_the_cage if 0 <= i + x < self.N and 0 <= j + y < self.N))
#
#     def show(self):
#         ...
#         for i in self.pole:
#             print(*map(lambda j: "#" if not j.fl_open else j.around_mines if not j.mine else "$", i))
#
#
# pole_game = GamePole(10, 12)

from random import randint


class Cell:
    def __init__(self, around_mines=0, mine=False, fl_open=False):
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = fl_open


class GamePole:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.pole = [[Cell() for n in range(self.N)] for n in range(self.N)]

    def init(self):
        for i in range(self.M):
            random_1 = randint(0, self.N - 1)
            random_2 = randint(0, self.N - 1)
            self.pole[random_1][random_2] = Cell(mine=True)

    def show(self):
        pass


pole_game = GamePole(10, 12)

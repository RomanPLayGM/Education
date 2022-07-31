from sys import stdin


class Matrix(list):
    def __init__(self, ls):
        super().__init__()
        self.ls = [line.copy() for line in ls]

    def __str__(self):
        return '\n'.join(['\t'.join(map(str, line)) for line in self.ls])

    def size(self):
        return len(self.ls), len(self.ls[0])

    def __add__(self, other):
        return Matrix(
            [list(map(sum, zip(*i))) for i in zip(self.ls, other.ls)]
        )

    def __mul__(self, other):
        return Matrix([list(map(lambda x: x * other, i)) for i in self.ls])

    __rmul__ = __mul__


exec(stdin.read())

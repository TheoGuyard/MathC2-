from copy import deepcopy
from math import sqrt
from random import shuffle, randint

class Sudoku:
    
    def __init__(self, n: int):
        assert sqrt(n) == int(sqrt(n)), "n n'est pas un carré !"
        self.n = n
        self.b = int(sqrt(self.n))
        self.X = [[[0 for k in range(n)] for j in range(n)] for i in range(n)]
        self.initialize_diagonal()
        while True:
            self.solve()
            if not self.grid_is_valid():
                self.empty_grid()
                self.initialize_diagonal()
            else:
                break
        self.X0 = deepcopy(self.X)

    def empty_grid(self):
        self.X = [[[0 for k in range(self.n)] for j in range(self.n)] for i in range(self.n)]

    def initialize_diagonal(self):
        B = []
        for bb in range(0, self.n, self.b):
            numbers = [i for i in range(self.n)]
            shuffle(numbers)
            for i, number in enumerate(numbers):
                self.X[bb + i // self.b][bb + i % self.b][number] = 1

    def print_grid(self):
        print(self)

    def mask(self, p: float = 0.5):
        m = round(p * self.n**2)
        masked = []
        for mi in range(m):
            while True:
                i = randint(0, self.n - 1)
                j = randint(0, self.n - 1)
                if not (i, j) in masked:
                    self.X[i][j] = [0 for _ in range(self.n)]
                    masked.append((i, j))
                    break
        self.X0 = deepcopy(self.X)

    def find_empty_position(self):
        for i in range(self.n):
            for j in range(self.n):
                if not any(self.X[i][j]):
                    return (i, j)
        return None

    def is_fillable_with(self, i: int, j: int, k: int) -> bool:
        for c in range(self.n):
            if self.X[i][c][k] == 1 and j != c:
                return False
        for l in range(len(self.X[0])):
            if self.X[l][j][k] == 1 and i != l:
                return False
        cube_x = j // self.b
        cube_y = i // self.b
        for l in range(cube_y * self.b, cube_y * self.b + self.b):
            for c in range(cube_x * self.b, cube_x * self.b + self.b):
                if self.X[l][c][k] == 1 and (l,c) != (i, j):
                    return False
        return True

    def grid_is_valid(self) -> bool:
        for i in range(self.n):
            for j in range(self.n):
                if sum(self.X[i][j]) != 1:
                    return False
        for i in range(self.n):
            for k in range(self.n):
                if sum(self.X[i][j][k] for j in range(self.n)) != 1:
                    return False
        for j in range(self.n):
            for k in range(self.n):
                if sum(self.X[i][j][k] for i in range(self.n)) != 1:
                    return False
        for i in range(self.n):
            for j in range(self.n):
                if i % self.b == j % self.b == 0: 
                    for k in range(self.n):  
                        if sum(self.X[ib][jb][k] for ib in range(i, i + self.b) for jb in range(j, j + self.b)) != 1:
                            return False
        return True

    def solve(self, verbosity: bool = False):

        if verbosity:
            print("RESOLUTION ...")
            print(self)
            print()

        empty_position = self.find_empty_position()
        if not empty_position:
            return True
        else:
            i, j = empty_position

        for k in range(self.n):
            if self.is_fillable_with(i, j, k):
                self.X[i][j][k] = 1
                if self.solve(verbosity=verbosity):
                    return True
                self.X[i][j][k] = 0
        return False

    def __str__(self):
        colspace = len(str(self.n)) + 1
        result = ""
        result += ("+-" + "-" * colspace * self.b) * self.b + "+\n"
        for i in range(self.n):
            result += "| "
            for j in range(self.n):
                vals = [k for k in range(self.n) if self.X[i][j][k] == 1]
                if len(vals) == 0:
                    k = " " * colspace
                elif len(vals) == 1:
                    k = " " * (colspace - len(str(vals[0] + 1)) - 1) + str(vals[0] + 1) + " "
                else:
                    k = "?" + " " * (colspace - 1)
                result += k
                if j in range(self.b-1,self.n-1,self.b):
                    result += "| "
            result += "|\n"
            if (i + 1) % self.b == 0 and i != self.n - 1:
                result += ("+-" + "-" * colspace * self.b) * self.b + "+\n"
        result += ("+-" + "-" * colspace * self.b) * self.b + "+"
        return result

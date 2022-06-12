import numpy as np
from math import sqrt
from pyomo.environ import *

CPLEX_PATH = "/Applications/CPLEX_Studio201/cplex/bin/x86-64_osx/cplex"

class Sudoku:
    
    def __init__(self, n):
        assert sqrt(n) == int(sqrt(n)), "n n'est pas un carré !"
        self.n = n
        self.b = int(sqrt(self.n))
        self.X = np.zeros((self.n, self.n, self.n), dtype=int)
        self.initialize_diagonal()
        while True:
            valid = self.solve()
            if not valid:
                self.empty_grid()
                self.initialize_diagonal()
            else:
                break

    def empty_grid(self):
        self.X = np.zeros((self.n, self.n, self.n), dtype=int)

    def initialize_diagonal(self):
        B = []          # Ensemble des blocs de la grille
        for bb in range(0, self.n, self.b):
            numbers = np.arange(self.n)
            np.random.shuffle(numbers)
            numbers = numbers.reshape(self.b, self.b)
            for i in range(self.b):
                for j in range(self.b):
                    self.X[bb + i, bb + j, numbers[i, j]] = 1

    def print_grid(self):
        print(self)

    def mask(self, p=0.5):
        m = round(p * self.n**2)
        masked = []
        for mi in range(m):
            while True:
                i = np.random.randint(0, self.n)
                j = np.random.randint(0, self.n)
                if not (i, j) in masked:
                    self.X[i, j, :] = 0
                    masked.append((i, j))
                    break

    def solve(self):
        n = self.n
        b = int(sqrt(n))
        N = list(range(1, n+1))

        model = ConcreteModel()
        model.x = Var(N, N, N, within = Binary)

        # Assignment constraint
        model.allcell_constr = ConstraintList()
        for i in N:
            for j in N:
                model.allcell_constr.add(1 == sum(model.x[i, j, k] for k in N))

        # Row constraint
        model.row_constr = ConstraintList()
        for i in N:
            for k in N:
                model.row_constr.add(1 == sum(model.x[i, j, k] for j in N))
            
        # Column constraint
        model.col_constr = ConstraintList()
        for j in N:
            for k in N:
                model.col_constr.add(1 == sum(model.x[i, j, k] for i in N))
            
        # Block constraint
        model.blk_constr = ConstraintList()
        for i in list(range(1, n, b)):
            i_blk = range(i, i+b)
            for j in list(range(1, n, b)):
                j_blk = range(j, j+b)
                for k in N:
                    model.blk_constr.add(1 == sum(model.x[p, q, k] for p in i_blk for q in j_blk))
            
        # Initial constraint
        model.initcell_constr = ConstraintList()
        for i in N:
            for j in N:
                if np.sum(self.X[i-1, j-1, :]) == 1:
                    k = np.where(self.X[i-1, j-1, :])[0][0] + 1
                    model.initcell_constr.add(1 == model.x[i,j,k])
            
        # Objective function
        model.Obj = Objective(expr = summation(model.x), sense=minimize)

        # Solving 
        opt = SolverFactory('cplex', executable=CPLEX_PATH)
        res = opt.solve(model)

        # Recover the grid
        for i in N:
            for j in N:
                for k in N:
                    if model.x[i,j,k]() == 1:
                        self.X[i-1, j-1, k-1] = 1

        return res.solver.termination_condition == TerminationCondition.optimal

    def __str__(self):
        colspace = len(str(self.n)) + 1
        result = ""
        result += ("+-" + "-" * colspace * self.b) * self.b + "+\n"
        for i in range(self.n):
            result += "| "
            for j in range(self.n):
                vals = np.where(self.X[i, j, :] == 1)[0]
                if vals.size == 0:
                    k = " " * colspace
                elif vals.size == 1:
                    k = " " * (colspace - len(str(vals[0] + 1)) - 1) + str(vals[0] + 1) + " "
                else:
                    k = " " * (colspace - 1) + "?"
                result += k
                if j in range(self.b-1,self.n-1,self.b):
                    result += "| "
            result += "|\n"
            if (i + 1) % self.b == 0 and i != self.n - 1:
                result += ("+-" + "-" * colspace * self.b) * self.b + "+\n"
        result += ("+-" + "-" * colspace * self.b) * self.b + "+"
        return result

from sudoku import Sudoku
from solveur import solveur
from verificateur import verificateur

sudoku = Sudoku(9)

print("SUDOKU INITIAL")
print(sudoku)

print()
print("SUDOKU MASQUÉ")
sudoku.mask(0.5)
print(sudoku)
print()

# sudoku.solve(verbosity=False)
solveur(sudoku)

print("SUDOKU RÉSOLU ")
print(sudoku)
verificateur(sudoku)
from sudoku import Sudoku
from verificateur import verificateur

sudoku = Sudoku(9)

print()
print("SUDOKU INITIAL")
print(sudoku)

print()
print("SUDOKU MASQUÉ")
sudoku.mask(0.5)
print(sudoku)

print()
print("SUDOKU RÉSOLU")
sudoku.solve()
print(sudoku)

verificateur(sudoku)
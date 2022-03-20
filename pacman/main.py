from MIPT_TP_PROJECT.pacman.field import Cell, Field
from MIPT_TP_PROJECT.pacman.interface import *
from MIPT_TP_PROJECT.pacman.move import *
from MIPT_TP_PROJECT.pacman.game import *

mas = [0]*5
for i in range(5):
    mas[i] = [0]*5
for i in range(5):
    for j in range(5):
        if i == 2 and j == 2:
            mas[i][j] = Cell(Pacman("i"), i, j)
        elif i == 3 and j == 3 or i == 2 and j == 3 or i == 4 and j == 2:
            mas[i][j] = Cell(Ghost(), i, j)
        elif i > 3:
            mas[i][j] = Cell(Dot(), i, j)
        else:
            mas[i][j] = Cell(Empty(), i, j)
field = Field(mas)
move = Move(field, GhostLevel.EASY_GHOST)
inter = ConsoleInterface()
game = Game(move, inter)
inter.draw(field)
game.play()


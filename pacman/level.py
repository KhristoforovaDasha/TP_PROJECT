from abc import ABCMeta, abstractmethod
import info as info
from object import Pacman, Ghost, Empty, Dot, Wall
from field import Cell, Field


def field_init(game_level):
    level = None
    if game_level == "easy":
        level = EasyLevel()
    elif game_level == "medium":
        level = MediumLevel()
    elif game_level == "hard":
        level = HardLevel()
    return Field(level.field_init())


class Level:
    __metaclass__ = ABCMeta

    @abstractmethod
    def field_init(self):
        """создать поле"""


class EasyLevel(Level):
    def field_init(self):
        info.dots = 0
        mas = [[]] * info.height
        for i in range(info.height):
            mas[i] = [None]*info.height
        for i in range(info.height):
            for j in range(info.width):
                if i == 4 and j == 2:
                    mas[i][j] = Cell(Pacman("Player"), i, j)
                elif i == 1 and j == 2:
                    mas[i][j] = Cell(Ghost(info.RED), i, j)
                elif i == 2 and j == 2:
                    mas[i][j] = Cell(Ghost(info.BLUE), i, j)
                elif i == 3 and j == 2:
                    mas[i][j] = Cell(Ghost(info.YELLOW), i, j)
                elif i == 3 and j == 2 or i == 1 and j == 1:
                    mas[i][j] = Cell(Wall("down"), i, j)
                elif i == 2 and j == 3:
                    mas[i][j] = Cell(Wall("right"), i, j)
                else:
                    mas[i][j] = Cell(Dot(), i, j)
                    info.dots += 1
        return mas


class MediumLevel(Level):

    def field_init(self):
        info.dots = 0
        info.height = info.MEDIUM_LEVEL_HEIGHT
        info.width = info.MEDIUM_LEVEL_WIDTH
        info.scale = info.WINDOW_SIZE/info.height
        info.SQUARE_SIZE = info.scale
        mas = [[]] * info.height
        for i in range(info.height):
            mas[i] = [None] * info.height
        for i in range(info.height):
            for j in range(info.width):
                if i == 3 and j == 4 or i == 5 and j == 5:
                    mas[i][j] = Cell(Ghost(info.RED), i, j)
                elif i == 4 and j == 4 or i == 3 and j == 5:
                    mas[i][j] = Cell(Ghost(info.BLUE), i, j)
                elif i == 5 and j == 4 or i == 4 and j == 5:
                    mas[i][j] = Cell(Ghost(info.YELLOW), i, j)
                elif i == 5 and j == 7:
                    mas[i][j] = Cell(Pacman("Player"), i, j)
                elif 1 <= i <= 2 and (1 <= j <= 2 or 7 <= j <= 8) or 7 <= i <= 8 and (1 <= j <= 2 or 7 <= j <= 8):
                    mas[i][j] = Cell(Dot(), i, j)
                    info.dots += 1
                elif i == 4 and (j == 2 or j == 6) or i == 1 and j == 6:
                    mas[i][j] = Cell(Wall("down"), i, j)
                elif i == 1 and j == 4 or i == 5 and j == 1 or i == 8 and j == 6:
                    mas[i][j] = Cell(Wall("right"), i, j)
                else:
                    mas[i][j] = Cell(Empty(), i, j)
        return mas


class HardLevel(Level):
    def field_init(self):
        info.dots = 0
        info.height = info.HARD_LEVEL_HEIGHT
        info.width = info.HARD_LEVEL_WIDTH
        info.scale = info.WINDOW_SIZE / info.height
        info.SQUARE_SIZE = info.scale
        mas = [[]] * info.height
        for i in range(info.height):
            mas[i] = [None] * info.height
        for i in range(info.height):
            for j in range(info.width):
                if i == 5 and j == 6 or i == 7 and j == 7:
                    mas[i][j] = Cell(Ghost(info.RED), i, j)
                elif i == 6 and j == 6 or i == 5 and j == 7:
                    mas[i][j] = Cell(Ghost(info.BLUE), i, j)
                elif i == 7 and j == 6 or i == 6 and j == 7:
                    mas[i][j] = Cell(Ghost(info.YELLOW), i, j)
                elif 1 <= j <= 2 and 2 <= i <= 4 or 3 <= j <= 4 and 1 <= i <= 3 or j == 7 and i == 1 or 6 <= j <= 7 and 10 <= i <= 11 or j == 1 and i == 9 or 12 <= j <= 13 and 1 <= i <= 2:
                    mas[i][j] = Cell(Dot(), i, j)
                    info.dots += 1
                elif 7 <= j <= 9 and i == 2 or 5 <= j <= 7 and j == 12 or 1 <= j <= 3 and i == 5 or 11 <= j <= 13 and i == 5:
                    mas[i][j] = Cell(Wall("right"), i, j)
                elif j == 12 and 8 <= i <= 11 or j == 8 and 5 <= i <= 7 or j == 3 and 9 <= i <= 11:
                    mas[i][j] = Cell(Wall("down"), i, j)
                elif i == 10 and j == 10:
                    mas[i][j] = Cell(Pacman("Player"), i, j)
                else:
                    mas[i][j] = Cell(Empty(), i, j)
        return mas

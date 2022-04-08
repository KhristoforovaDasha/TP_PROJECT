from random import randint
from MIPT_TP_PROJECT.pacman.object import *
from MIPT_TP_PROJECT.pacman.game import *


class Move:
    def __init__(self, field, level):
        self.field = field
        self.level = level

    @staticmethod
    def is_correct(pos_x, pos_y):
        return bool(0 <= pos_x < Info.height and 0 <= pos_y < Info.width)

    def easy_move_ghost(self, x, y):
        pos_x = x + randint(-1, 1)
        pos_y = y + randint(-1, 1)
        if Move.is_correct(pos_x, pos_y):
            obj_type = self.field.get_obj_type(pos_x, pos_y)
            if obj_type == ObjType.OBJ_EMPTY:
                self.field.cell[pos_x][pos_y].obj, self.field.cell[x][y].obj = \
                    self.field.cell[x][y].obj, self.field.cell[pos_x][pos_y].obj
            elif obj_type == ObjType.OBJ_PACMAN:
                self.field.cell[pos_x][pos_y].obj.decrease_life_count()
                if self.field.cell[pos_x][pos_y].obj.get_life_count() != 0:
                    Game.stop_game = ExitGame.STOP
                else:
                    Game.stop_game = ExitGame.EXIT_LOST

    def step(self):
        for x in range(Info.height):
            for y in range(Info.width):
                if self.field.get_obj_type(x, y) == ObjType.OBJ_GHOST:
                    if self.level == GhostLevel.EASY_GHOST:
                        self.easy_move_ghost(x, y)
                    elif self.level == GhostLevel.MEDIUM_GHOST:
                        pass
                    else:
                        pass

    def move_right(self, x, y):
        pass

    def move_left(self, x, y):
        pass

    def move_down(self, x, y):
        pass

    def move_up(self, x, y):
        pass

    def do_move(self, x, y, delta_x, delta_y):
        if self.field.get_obj_type(x + delta_x, y + delta_y) == ObjType.OBJ_GHOST:
            self.field.cell[x][y].obj.decrease_life_count()
            Game.stop_game = ExitGame.STOP
        else:
            if self.field.get_obj_type(x + delta_x, y + delta_y) == ObjType.OBJ_DOT:
                self.field.cell[x][y].obj.pacman_score += 1
                self.field.cell[x + delta_x][y + delta_y].obj = Empty()
            if self.field.cell[x][y].obj.pacman_score == Info.dots:
                Game.stop_game = ExitGame.EXIT_WON
            self.field.cell[x + delta_x][y + delta_y].obj, self.field.cell[x][y].obj = \
                self.field.cell[x][y].obj, self.field.cell[x + delta_x][y + delta_y].obj

    def move_pac(self, place):
        is_move = 0
        for x in range(Info.height):
            for y in range(Info.width):
                if self.field.get_obj_type(x, y) == ObjType.OBJ_PACMAN:
                    if place == 'right' and Move.is_correct(x, y + 1):
                        self.do_move(x, y, 0, 1)
                    elif place == "left" and Move.is_correct(x, y - 1):
                        self.do_move(x, y, 0, -1)
                    elif place == "up" and Move.is_correct(x - 1, y):
                        self.do_move(x, y, -1, 0)
                    elif place == "down" and Move.is_correct(x + 1, y):
                        self.do_move(x, y, 1, 0)
                    is_move = 1
                    break
                if is_move:
                    break

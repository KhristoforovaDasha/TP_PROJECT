from random import randint
from object import *
from game import *
import info as info


class Move:
    def __init__(self, field):
        self.field = field

    @staticmethod
    def is_correct(pos_x, pos_y):
        return bool(0 <= pos_x < info.height and 0 <= pos_y < info.width)

    def change(self, pos_x, pos_y, x, y):
        self.field.cell[pos_x][pos_y].obj_second = self.field.cell[x][y].obj
        self.field.cell[pos_x][pos_y].obj, self.field.cell[pos_x][pos_y].obj_second = \
            self.field.cell[pos_x][pos_y].obj_second, self.field.cell[pos_x][pos_y].obj
        self.field.cell[x][y].obj = Empty()

    def easy_move_ghost(self, x, y):
        pos_x = x + randint(-1, 1)
        pos_y = y + randint(-1, 1)
        if Move.is_correct(pos_x, pos_y):
            obj_type = self.field.get_obj_type(pos_x, pos_y)
            if obj_type == ObjType.OBJ_EMPTY:
                self.field.cell[pos_x][pos_y].obj, self.field.cell[x][y].obj = \
                    self.field.cell[x][y].obj, self.field.cell[pos_x][pos_y].obj
            elif obj_type != ObjType.OBJ_GHOST:
                game_life = None
                if obj_type == ObjType.OBJ_PACMAN:
                    self.field.cell[pos_x][pos_y].obj.decrease_life_count()
                    game_life = self.field.cell[pos_x][pos_y].obj.get_life_count()
                    Move.change_game_state(game_life)
                if self.field.get_obj_type(pos_x, pos_y) != ObjType.OBJ_WALL or not Move.block(pos_x - x, pos_y - y, self.field.cell[pos_x][pos_y].obj.get_place()):
                    self.change(pos_x, pos_y, x, y)
                return game_life

    def step(self):
        game_life = 0
        for x in range(info.height):
            for y in range(info.width):
                obj_type = self.field.get_obj_type(x, y)
                if obj_type == ObjType.OBJ_GHOST:
                    game_life = self.easy_move_ghost(x, y)
        return game_life

    def move_right(self, x, y):
        pass

    def move_left(self, x, y):
        pass

    def move_down(self, x, y):
        pass

    def move_up(self, x, y):
        pass

    @staticmethod
    def block(delta_x, delta_y, place):
        if delta_x == 1 and delta_y == 0:
            return place == "left"
        if delta_x == -1 and delta_y == 0:
            return place == "right"
        if delta_x == 0 and delta_y == 1:
            return place == "up"
        if delta_x == 0 and delta_y == -1:
            return place == "down"

    @staticmethod
    def change_game_state(game_life):
        if game_life > 0:
            Game.set_state(ExitGame.STOP)
        else:
            Game.set_state(ExitGame.EXIT_LOST)

    def do_move(self, x, y, delta_x, delta_y):
        game_life = self.field.cell[x][y].obj.get_life_count()
        if self.field.get_obj_type(x + delta_x, y + delta_y) == ObjType.OBJ_GHOST:
            self.field.cell[x][y].obj.decrease_life_count()
            self.field.cell[x + delta_x][y + delta_y].obj_second = self.field.cell[x][y].obj
            self.field.cell[x][y].obj = Empty()
            game_life = self.field.cell[x + delta_x][y + delta_y].obj_second.get_life_count()
            Move.change_game_state(game_life)
            return self.field.cell[x + delta_x][y + delta_y].obj_second.get_score(), game_life
        else:
            obj_type = self.field.get_obj_type(x + delta_x, y + delta_y)
            obj_second_type = self.field.get_obj_second_type(x + delta_x, y + delta_y)
            if obj_type == ObjType.OBJ_DOT or obj_second_type == ObjType.OBJ_DOT:
                if obj_second_type == ObjType.OBJ_DOT:
                    self.field.cell[x + delta_x][y + delta_y].obj, self.field.cell[x + delta_x][y + delta_y].obj_second = \
                        self.field.cell[x + delta_x][y + delta_y].obj_second, self.field.cell[x + delta_x][y + delta_y].obj
                print(self.field.cell[x][y].obj.get_score())
                self.field.cell[x][y].obj.increase_score()
                self.field.cell[x + delta_x][y + delta_y].obj = Empty()
            if self.field.cell[x][y].obj.get_score() == info.dots:
                Game.stop_game = ExitGame.EXIT_WON
            if self.field.get_obj_type(x + delta_x, y + delta_y) != ObjType.OBJ_WALL:
                self.field.cell[x + delta_x][y + delta_y].obj, self.field.cell[x][y].obj = \
                    self.field.cell[x][y].obj, self.field.cell[x + delta_x][y + delta_y].obj
            elif not Move.block(delta_x, delta_y, self.field.cell[x + delta_x][y + delta_y].obj.get_place()):
                self.change(x + delta_x, y + delta_y, x, y)
            return self.field.cell[x + delta_x][y + delta_y].obj.get_score(), game_life

    def move_pac(self, place):
        for x in range(info.height):
            for y in range(info.width):
                if self.field.get_obj_type(x, y) == ObjType.OBJ_PACMAN:
                    if place == 'right' and Move.is_correct(x, y + 1):
                        return self.do_move(x, y, 0, 1)
                    elif place == "left" and Move.is_correct(x, y - 1):
                        return self.do_move(x, y, 0, -1)
                    elif place == "up" and Move.is_correct(x - 1, y):
                        return self.do_move(x, y, -1, 0)
                    elif place == "down" and Move.is_correct(x + 1, y):
                        return self.do_move(x, y, 1, 0)
                    else:
                        return self.field.cell[x][y].obj.get_score(), self.field.cell[x][y].obj.get_life_count()

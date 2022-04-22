from object import *


class Cell:
    def __init__(self, obj, pos_x, pos_y):
        self.obj = obj
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.obj_second = Empty()


class Field:
    def __init__(self, cell):
        self.cell = cell

    def get_obj_type(self, pos_x, pos_y):
        return self.cell[pos_x][pos_y].obj.get_type()

    def get_obj_second_type(self, pos_x, pos_y):
        return self.cell[pos_x][pos_y].obj_second.get_type()

    def get_obj_colour(self, pos_x, pos_y):
        return self.cell[pos_x][pos_y].obj.get_colour()

    def get_obj_second_colour(self, pos_x, pos_y):
        return self.cell[pos_x][pos_y].obj_second.get_colour()

    def get_cell(self, pos_x, pos_y):
        return self.cell[pos_x][pos_y]

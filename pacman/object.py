from info import *
from abc import ABCMeta, abstractmethod


class GameObject:
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_type(self):
        """возвратить имя объекта"""

    @abstractmethod
    def get_colour(self):
        """возвратить цвет объекта"""


class Pacman(GameObject):
    __type = ObjType.OBJ_PACMAN
    __colour = ObjColour.COL_PACMAN

    def __init__(self, name):
        self.name = name
        self.pacman_score = 0
        self.pacman_life = LIVE

    def get_type(self):
        return self.__type

    def get_colour(self):
        return self.__colour

    def decrease_life_count(self):
        self.pacman_life -= 1

    def get_life_count(self):
        return self.pacman_life

    def get_score(self):
        return self.pacman_score

    def set_score(self, score):
        self.pacman_score = score

    def set_life(self, life):
        self.pacman_life = life

    def increase_score(self):
        self.pacman_score += 1

    def increase_and_get_score(self):
        self.pacman_score += 1
        return self.pacman_score


class Ghost(GameObject):
    __type = ObjType.OBJ_GHOST

    def __init__(self, color):
        self.color = color

    def get_type(self):
        return self.__type

    def get_colour(self):
        return self.color


class Dot(GameObject):
    __type = ObjType.OBJ_DOT
    __colour = ObjColour.COL_DOT

    def get_type(self):
        return self.__type

    def get_colour(self):
        return self.__colour


class Wall(GameObject):
    __type = ObjType.OBJ_WALL
    __colour = ObjColour.COL_WALL

    def __init__(self, place):
        self.place = place

    def get_place(self):
        return self.place

    def get_type(self):
        return self.__type

    def get_colour(self):
        return self.__colour


class Empty(GameObject):
    __type = ObjType.OBJ_EMPTY
    __colour = ObjColour.COL_EMPTY

    def get_type(self):
        return self.__type

    def get_colour(self):
        return self.__colour

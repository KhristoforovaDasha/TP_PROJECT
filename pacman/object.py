from MIPT_TP_PROJECT.pacman.info import *
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
        self.__pacman_life = 3

    def get_type(self):
        return self.__type

    def get_colour(self):
        return self.__colour

    def decrease_life_count(self):
        self.__pacman_life -= 1

    def get_life_count(self):
        return self.__pacman_life


class Ghost(GameObject):
    __type = ObjType.OBJ_GHOST
    __colour = ObjColour.COL_GHOST

    def get_type(self):
        return self.__type

    def get_colour(self):
        return self.__colour


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

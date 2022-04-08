from enum import Enum


class GhostLevel(Enum):
    EASY_GHOST = 1
    MEDIUM_GHOST = 2
    HARD_GHOST = 3


class ObjColour(Enum):
    COL_PACMAN = 1
    COL_GHOST = 2
    COL_DOT = 3
    COL_WALL = 4
    COL_EMPTY = 5


class ObjType(Enum):
    OBJ_PACMAN = 1
    OBJ_GHOST = 2
    OBJ_DOT = 3
    OBJ_WALL = 4
    OBJ_EMPTY = 5


class ObjPicture(Enum):
    PICTURE_PACMAN = '@'
    PICTURE_GHOST = '^'
    PICTURE_DOT = '.'
    PICTURE_WALL = '_'
    PICTURE_EMPTY = '*'


class Info:
    width = 5
    height = 5
    dots = 4


class ExitGame:
    EXIT_WON = 1
    EXIT_LOST = 2
    STOP = 3
    CONTINUE = 4

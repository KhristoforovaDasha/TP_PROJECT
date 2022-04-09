from enum import Enum
import pygame.transform


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


FPS = 60
clock = pygame.time.Clock()
TEXT_SIZE = 24
TEXT_SIZE_INFO = 36
TEXT_FONT = None
WHITE = (255, 255, 255)
TEXT_SPACE = 30
message = "Number of your lives has decreased"
radius = 5
dots = 0
width = 5
height = 5
WINDOW_SIZE = 600
EASY_LEVEL_WIDTH = 5
EASY_LEVEL_HEIGHT = 5
MEDIUM_LEVEL_WIDTH = 10
MEDIUM_LEVEL_HEIGHT = 10
HARD_LEVEL_WIDTH = 15
HARD_LEVEL_HEIGHT = 15
scale = 100
BLACK = (0, 0, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 32, 255)
WIDTH_RET = 2
WIDTH_LINE = 10
SQUARE_SIZE = scale
LIVE = 3
TEXT_WIDTH = 200
TEXT_HEIGHT = 50
PACMAN = pygame.transform.scale(pygame.image.load('MIPT_TP_PROJECT/images/pacman.png'), (30, 30))
GHOST_RED = pygame.transform.scale(pygame.image.load('MIPT_TP_PROJECT/images/ghost_red.png'), (30, 30))
GHOST_YELLOW = pygame.transform.scale(pygame.image.load('MIPT_TP_PROJECT/images/ghost_yellow.png'), (30, 30))
GHOST_BLUE = pygame.transform.scale(pygame.image.load('MIPT_TP_PROJECT/images/ghost_blue.png'), (30, 30))
DOT_COLOUR = YELLOW
WALL_COLOUR = RED
WON_MESSAGE = "Game is over. You are won:)!"
LOST_MESSAGE = "Game is over. You are lost:(!"


class ExitGame:
    EXIT_WON = 1
    EXIT_LOST = 2
    STOP = 3
    CONTINUE = 4


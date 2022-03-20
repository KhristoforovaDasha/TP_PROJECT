from abc import ABCMeta, abstractmethod
from MIPT_TP_PROJECT.pacman.info import *


class Interface:
    __metaclass__ = ABCMeta

    @abstractmethod
    def read(self):
        """read some information"""

    @abstractmethod
    def draw(self, field):
        """draw the field"""


class ConsoleInterface(Interface):

    def read(self):
        return input()

    def draw(self, field):
        for x in range(Info.height):
            for y in range(Info.width):
                obj_type = field.get_obj_type(x, y)
                if obj_type == ObjType.OBJ_PACMAN:
                    print(ObjPicture.PICTURE_PACMAN.value, end=" ")
                elif obj_type == ObjType.OBJ_GHOST:
                    print(ObjPicture.PICTURE_GHOST.value, end=" ")
                elif obj_type == ObjType.OBJ_DOT:
                    print(ObjPicture.PICTURE_DOT.value, end=" ")
                elif obj_type == ObjType.OBJ_EMPTY:
                    print(ObjPicture.PICTURE_EMPTY.value, end=" ")
                else:
                    print(ObjPicture.PICTURE_WALL.value, end=" ")
            print()
        print()


class GraphicInterface(Interface):
    def read(self):
        pass

    def draw(self, field):
        pass


class TelegramInterface(Interface):
    def read(self):
        pass

    def draw(self, field):
        pass

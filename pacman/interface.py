from abc import ABCMeta, abstractmethod
from info import *
import pygame
from time import sleep
import info as info


def interface_init(interface_type):
    if interface_type == "graphic":
        pygame.init()
        screen = pygame.display.set_mode((info.width * info.scale, info.height * info.scale + TEXT_SPACE))
        pygame.display.set_caption('Pacman')
        return GraphicInterface(screen)
    elif interface_type == "console":
        return ConsoleInterface()


class Interface:
    __metaclass__ = ABCMeta

    @abstractmethod
    def read(self):
        """read some information"""

    @abstractmethod
    def draw(self, field, score, life):
        """draw the field"""

    @abstractmethod
    def stop(self, field, score, life):
        """print stop message"""

    @abstractmethod
    def exit(self, text):
        """print end message"""


class ConsoleInterface(Interface):

    def read(self):
        inp = input()
        if inp == "right":
            return "down"
        elif inp == "left":
            return "up"
        elif inp == "down":
            return "right"
        elif inp == "up":
            return "left"

    def draw(self, field, score=0, life=LIVE):
        print("Your number of life: " + str(life) + "     " + "Your game score: " + str(score))
        for x in range(info.height):
            for y in range(info.width):
                obj_type = field.get_obj_type(y, x)
                obj_second_type = field.get_obj_second_type(x, y)
                if obj_second_type == ObjType.OBJ_GHOST:
                    print(ObjPicture.PICTURE_GHOST.value, end=" ")
                if obj_second_type == ObjType.OBJ_WALL:
                    print(ObjPicture.PICTURE_WALL.value, end=" ")
                if obj_second_type == ObjType.OBJ_DOT:
                    print(ObjPicture.PICTURE_DOT.value, end=" ")
                if obj_type == ObjType.OBJ_PACMAN:
                    print(ObjPicture.PICTURE_PACMAN.value, end="   ")
                elif obj_type == ObjType.OBJ_GHOST:
                    print(ObjPicture.PICTURE_GHOST.value, end="   ")
                elif obj_type == ObjType.OBJ_DOT:
                    print(ObjPicture.PICTURE_DOT.value, end="   ")
                elif obj_type == ObjType.OBJ_EMPTY:
                    print(ObjPicture.PICTURE_EMPTY.value, end="   ")
                else:
                    print(ObjPicture.PICTURE_WALL.value, end="   ")
            print()
        print()

    def stop(self, field, score, life):
        print(message)
        self.draw(field, score, life)

    def exit(self, text):
        print(text)
        exit()


class GraphicInterface(Interface):
    def __init__(self, screen):
        self.screen = screen

    def read(self):
        while True:
            clock.tick(FPS)
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        pygame.event.clear()
                        return "up"
                    elif event.key == pygame.K_RIGHT:
                        pygame.event.clear()
                        return "down"
                    elif event.key == pygame.K_DOWN:
                        pygame.event.clear()
                        return "right"
                    elif event.key == pygame.K_UP:
                        pygame.event.clear()
                        return "left"
                else:
                    pygame.event.clear()

    def draw_ghost(self, obj_color, pos_x, pos_y):
        if obj_color == RED:
            ghost = GHOST_RED
        elif obj_color == BLUE:
            ghost = GHOST_BLUE
        elif obj_color == YELLOW:
            ghost = GHOST_YELLOW
        self.screen.blit(ghost, (pos_x + info.SQUARE_SIZE // 4, pos_y + info.SQUARE_SIZE // 4))

    def draw_wall(self, place, pos_x, pos_y):
        delta_x = info.SQUARE_SIZE if place == "right" else 0
        delta_y = info.SQUARE_SIZE if place == "down" else 0
        delta_end_y = info.SQUARE_SIZE if place == "left" or place == "right" else 0
        delta_end_x = info.SQUARE_SIZE if place == "up" or place == "down" else 0
        pygame.draw.line(self.screen, WALL_COLOUR, (pos_x + delta_x, pos_y + delta_y),
                         (pos_x + delta_x + delta_end_x, pos_y + delta_y + delta_end_y),
                         info.WIDTH_LINE)

    def draw(self, field, score=0, life=LIVE):
        self.screen.fill(BLACK)
        pygame.display.update()
        self.game_info(life, score)
        for x in range(info.height):
            pos_x = x * info.SQUARE_SIZE
            for y in range(info.width):
                obj_type = field.get_obj_type(x, y)
                obj_second_type = field.get_obj_second_type(x, y)
                pos_y = y * info.SQUARE_SIZE + TEXT_SPACE
                pygame.draw.rect(self.screen, BLUE,
                                 (pos_x, pos_y, pos_x + info.SQUARE_SIZE, pos_y + info.SQUARE_SIZE - TEXT_SPACE), info.WIDTH_RET)
                pygame.display.update()
                if obj_second_type == ObjType.OBJ_GHOST:
                    obj_color = field.get_obj_second_colour(x, y)
                    self.draw_ghost(obj_color, pos_x, pos_y)
                if obj_second_type == ObjType.OBJ_WALL:
                    place = field.get_cell(x, y).obj_second.place
                    self.draw_wall(place, pos_x, pos_y)
                if obj_second_type == ObjType.OBJ_DOT:
                    pygame.draw.circle(self.screen, DOT_COLOUR,
                                       (pos_x + info.SQUARE_SIZE // 2, pos_y + info.SQUARE_SIZE // 2),
                                       radius)
                if obj_type == ObjType.OBJ_PACMAN:
                    self.screen.blit(PACMAN, (pos_x + info.SQUARE_SIZE // 4, pos_y + info.SQUARE_SIZE // 4))
                elif obj_type == ObjType.OBJ_GHOST:
                    obj_color = field.get_obj_colour(x, y)
                    self.draw_ghost(obj_color, pos_x, pos_y)
                elif obj_type == ObjType.OBJ_DOT:
                    pygame.draw.circle(self.screen, DOT_COLOUR, (pos_x + info.SQUARE_SIZE // 2, pos_y + info.SQUARE_SIZE // 2),
                                       radius)
                elif obj_type == ObjType.OBJ_WALL:
                    place = field.get_cell(x, y).obj.place
                    self.draw_wall(place, pos_x, pos_y)
                pygame.display.update()

    def game_info(self, life, score):
        font = pygame.font.Font(TEXT_FONT, TEXT_SIZE)
        text = font.render(
            "Your number of life: " + str(life) + "     " + "Your game score: " + str(score), True, WHITE)
        place = text.get_rect()
        self.screen.blit(text, place)
        pygame.display.update()

    def write_message(self, text):
        self.screen.fill(BLACK)
        font = pygame.font.Font(TEXT_FONT, TEXT_SIZE_INFO)
        text_message = font.render(str(text), True, WHITE)
        place = text_message.get_rect(center=(250, 150))
        self.screen.blit(text_message, place)
        pygame.display.update()
        sleep(1)

    def stop(self, field, score, life):
        self.write_message(message)
        self.draw(field, score, life)

    def exit(self, text):
        self.write_message(text)
        pygame.quit()


class TelegramInterface(Interface):
    def read(self):
        pass

    def draw(self, field, score=0, life=LIVE):
        pass

    def stop(self, field, score, life):
        pass

    def exit(self, text):
        pass

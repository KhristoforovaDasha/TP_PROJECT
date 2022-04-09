from MIPT_TP_PROJECT.pacman.info import *
from copy import deepcopy
from object import Empty
import MIPT_TP_PROJECT.pacman.info as info
from MIPT_TP_PROJECT.pacman.interface import *
import sys


class Game:
    stop_game = ExitGame.CONTINUE
    begin_field = None
    game_life = LIVE

    def __init__(self, move, interface):
        self.move = move
        self.interface = interface
        Game.begin_field = deepcopy(move.field)

    @staticmethod
    def set_state(state):
        Game.stop_game = state

    def play(self):
        game_score = 0
        game_life = 0
        while True:
            inp = self.interface.read()
            game_score, game_life = self.move.move_pac(inp)
            self.interface.draw(self.move.field, game_score, game_life)
            if Game.stop_game != ExitGame.CONTINUE:
                break
            game_life_after_ghost_step = self.move.step()
            if game_life_after_ghost_step is None:
                self.interface.draw(self.move.field, game_score, game_life)
            else:
                self.interface.draw(self.move.field, game_score, game_life_after_ghost_step)
            if Game.stop_game != ExitGame.CONTINUE:
                break
        if Game.stop_game == ExitGame.STOP:
            self.stop(game_score, game_life)
        else:
            self.exit()

    def stop(self, game_score, game_life):
        self.begin_location()
        self.interface.stop(self.move.field, game_score, game_life)
        Game.stop_game = ExitGame.CONTINUE
        self.play()

    def begin_location(self):
        pacman_score = 0
        pacman_life = 0
        for i in range(height):
            for j in range(width):
                obj_type = self.move.field.get_obj_type(i, j)
                obj_second_type = self.move.field.get_obj_second_type(i, j)
                if obj_second_type == ObjType.OBJ_PACMAN:
                    pacman_score = self.move.field.cell[i][j].obj_second.get_score()
                    pacman_life = self.move.field.cell[i][j].obj_second.get_life_count()
                    self.move.field.cell[i][j].obj_second = Empty()
                if obj_type == ObjType.OBJ_GHOST:
                    self.move.field.cell[i][j].obj = Empty()
        for i in range(height):
            for j in range(width):
                obj_type = Game.begin_field.get_obj_type(i, j)
                if obj_type == ObjType.OBJ_PACMAN or obj_type == ObjType.OBJ_GHOST:
                    if obj_type == ObjType.OBJ_PACMAN:
                        Game.begin_field.cell[i][j].obj.set_score(pacman_score)
                        Game.begin_field.cell[i][j].obj.set_life(pacman_life)
                    self.move.field.cell[i][j].obj = deepcopy(Game.begin_field.cell[i][j].obj)

    def exit(self):
        if Game.stop_game == ExitGame.EXIT_WON:
            self.interface.exit(WON_MESSAGE)
        else:
            self.interface.exit(LOST_MESSAGE)
        if type(self.interface) == GraphicInterface:
            pygame.quit()
            sys.exit()


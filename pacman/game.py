from MIPT_TP_PROJECT.pacman.info import *


class Game:
    stop_game = ExitGame.CONTINUE
    begin_field = None

    def __init__(self, move, interface):
        self.move = move
        self.interface = interface
        Game.begin_field = move.field

    def play(self):
        while True:
            self.move.move_pac(self.interface.read())
            if Game.stop_game != ExitGame.CONTINUE:
                break
            self.interface.draw(self.move.field)
            self.move.step()
            if Game.stop_game != ExitGame.CONTINUE:
                break
            self.interface.draw(self.move.field)
        if Game.stop_game == ExitGame.STOP:
            self.stop()
        else:
            self.exit()

    def stop(self):
        print("You number of lives has decreased")
        self.interface.draw(Game.begin_field)
        Game.stop_game = ExitGame.CONTINUE
        self.play()

    @staticmethod
    def exit():
        if Game.stop_game == ExitGame.EXIT_WON:
            print("Game is over. You are won:)!")
        else:
            print("Game is over. You are lost:(!")


import MIPT_TP_PROJECT.pacman.interface as interface
from MIPT_TP_PROJECT.pacman.move import *
from MIPT_TP_PROJECT.pacman.game import *
import MIPT_TP_PROJECT.pacman.level as level


game_level = input()
interface_type = input()
field = level.field_init(game_level)
move = Move(field)
inter = interface.interface_init(interface_type)
game = Game(move, inter)
inter.draw(field)
game.play()


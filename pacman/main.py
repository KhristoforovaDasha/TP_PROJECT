import interface as interface
from move import *
from game import *
import level as level


game_level = input()
interface_type = input()
field = level.field_init(game_level)
move = Move(field)
inter = interface.interface_init(interface_type)
game = Game(move, inter)
inter.draw(field)
game.play()


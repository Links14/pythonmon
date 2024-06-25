# Trevor Loth
# 6-24-24
# Game class

import pkmClasses, pokedex, typeDict, moves
from math import floor
import random

class Game:
    
    def __init__(self, player, ai):
        self._user = player
        self._enemy = ai
    
    def player_switch_pokemon(self, newPokemon):
        self._user = newPokemon
    
    def ai_switch_pokemon(self, newPokemon):
        self._enemy = newPokemon
    
    def attack(self, user, target, move_slot):
        move = user.get_move(move_slot)         #list [movename, pp, maxpp]
        base_dmg = floor(floor(floor(2 * user.get_level() / 5 + 2) * moves.moves[move[0]] * user.get_atk() / user.get_def()) / 50) + 2;
        
        dmg = base_dmg * typeDict.getModifier(moves.moves[move[0]][0], target.get_typings())
    
    
# HP = floor(0.01 x (2 x Base + IV + floor(0.25 x EV)) x Level) + Level + 10
# Other Stats = (floor(0.01 x (2 x Base + IV + floor(0.25 x EV)) x Level) + 5) x Nature.    
    
    
if __name__ == "__main__":
    pkmn1 = pkmClasses.Pokemon(1, 15, 15, 5)
    pkmn2 = pkmClasses.Pokemon(4, 15, 15, 5)
    
    newGame = Game(pkmn2, pkmn1)
    
    Game.attack(pkmn1, pkmn2, input())



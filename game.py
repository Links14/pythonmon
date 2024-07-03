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
    
    def attack(user, target, move_slot:int):
        move = user.get_move(move_slot)         #list [movename, pp, maxpp]
        if type(move[0]) != str:
            print("Invalid move, defaulting to 0")
            move = user.get_move(0)
        elif move[1] <= 0:
            print("not enough pp")
            return
        
        #user.use_move(move_slot)
        base_dmg = floor(floor(floor(2 * user.get_level() / 5 + 2) * moves.moves[move[0]][0] * user.get_atk() / target.get_def()) / 50) + 2;
        
        dmg = base_dmg * typeDict.getModifier(moves.moves[move[0]][4], target.get_typings())
        
        print(user.get_activeHp(), " unga bunga")
        print(f"{user.get_name()} used {move[0]} and did {dmg} damage")
        
    
    #def show_stat_mods(self, player, enemy):
        
    
    
# HP = floor(0.01 x (2 x Base + IV + floor(0.25 x EV)) x Level) + Level + 10
# Other Stats = (floor(0.01 x (2 x Base + IV + floor(0.25 x EV)) x Level) + 5) x Nature.    
    
    
if __name__ == "__main__":
    user_pkmn = pkmClasses.Pokemon(1, 15, 5)
    ai_pkmn = pkmClasses.Pokemon(1, 15, 5)
    user_pkmn.set_moves_TEST([["tackle", 20, 20], [None, None, None], [None, None, None], [None, None, None]])
    ai_pkmn.set_moves_TEST([["tackle", 20, 20], [None, None, None], [None, None, None], [None, None, None]])
    
    newGame = Game(user_pkmn, ai_pkmn)
    
    try:
        select_move = int(input("Please enter one of the move slots (0 - 3): "))
    except:
        print("invalid input, defaulting to 0")
        select_move = 0
    
    Game.attack(user_pkmn, ai_pkmn, select_move)



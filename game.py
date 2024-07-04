# Trevor Loth
# 6-24-24
# Game class

import pkmClasses, pokedex, typeDict
from moves import moves
from math import floor
import random

class Game:
    
    def __init__(self, player, ai):
        self._user = player
        self._enemy = ai
        self.statchanges = {
                            "ATK"   : [0, 0],
                            "S.ATK" : [0, 0],
                            "DEF"   : [0, 0],
                            "S.DEF" : [0, 0],
                            "SPD"   : [0, 0],
                            "EVA"   : [0, 0],
                            "ACC"   : [0, 0]
                            }
        
    def reset_stat_changes(self, num):
        # 0 for user, 1 for enemy
        for i in self.statchanges.keys():
            self.statchanges[i][num] = 0
        
    def player_switch_pokemon(self, newPokemon):
        self._user = newPokemon
        self.reset_stat_changes(0)
    
    def ai_switch_pokemon(self, newPokemon):
        self._enemy = newPokemon
        self.reset_stat_changes(1)
    
    def use_move(self, user, target, move_slot:int):
        if move_slot > 3:
            print("Invalid move slot, defaulting to 0")
            move_slot = 0
        move = user.get_move(move_slot)         #list [movename, pp, maxpp]
        if type(move[0]) != str:
            print("Invalid move, defaulting to 0")
            move = user.get_move(0)
        elif move[1] <= 0:
            print("not enough pp")
            return
        
        print(moves[move[0]][3])
        base_dmg = floor(floor(floor(2 * user.get_level() / 5 + 2) * moves[move[0]][0] * user.get_atk() / target.get_def()) / 50) + 2;
        dmg = base_dmg * typeDict.getModifier(moves[move[0]][4], target.get_typings())
        print(f"{user.get_name()} used {move[0]} and did {dmg} damage\n {target.get_activeHp()}hp remaining")
        
        if dmg >= target.get_activeHp():
            self.on_faint(self, user, target)
        else:
            target.take_damage(dmg)
        
        
    def on_faint(self, user, target):
        print(f"{target.get_name()} has fainted")
        target.set_hp(0)

    #def show_stat_mods(self, player, enemy):

# HP = floor(0.01 x (2 x Base + IV + floor(0.25 x EV)) x Level) + Level + 10
# Other Stats = (floor(0.01 x (2 x Base + IV + floor(0.25 x EV)) x Level) + 5) x Nature.
    
    
if __name__ == "__main__":
    user_pkmn = pkmClasses.Pokemon(1, 50)
    ai_pkmn = pkmClasses.Pokemon(1, 50)
    print(user_pkmn.moves)
    user_pkmn.set_moves_TEST([["tackle", 20, 20], [None, None, None], [None, None, None], [None, None, None]])
    ai_pkmn.set_moves_TEST([["tackle", 20, 20], [None, None, None], [None, None, None], [None, None, None]])
    
    newGame = Game(user_pkmn, ai_pkmn)
    while (True):
        user_i = input("Please enter one of the move slots (0 - 3): ")
        try:
            select_move = int(user_i)
        except:
            if user_i == "exit":
                break
            print("invalid input, defaulting to 0")
            select_move = 0
        Game.use_move(Game, user_pkmn, ai_pkmn, select_move)



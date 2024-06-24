# Trevor Loth
# 6-23-24
# Pokémon and Pokédex class

import typeDict
import random

            # : ["",   [, , , , , ],   "",     "",     ,   ]
pokedex = { # EntryNum:int : ["name", [hp, atk, df, spatk, spdf, spd], ["type1", "type2"], evoLVL, evolutionEntry]
            1 : ["Bulbasaur",   [45, 49, 49, 65, 65, 45],   ["grass",    "poison"],     [],   16,     2],
            2 : ["Ivysaur",     [60, 62, 63, 80, 80, 60],   ["grass",    "poison"],     [],   32,     3],
            3 : ["Venosaur",    [80, 82, 83, 100, 100, 80], ["grass",    "poison"],     [],   None,   None],
            4 : ["Charmander",  [39, 52, 43, 60, 50, 65],   ["fire",     "none"],       [],   16,     5],
            5 : ["Charmeleon",  [58, 64, 58, 80, 65, 80],   ["fire",     "none"],       [],   36,     6],
            6 : ["Charizard",   [78, 84, 78, 109, 85, 100], ["fire",     "flying"],     [],   None,   None],
            7 : ["Squirtle",    [44, 48, 65, 50, 64, 43],   ["water",    "none"],       [],   16,     8],
            8 : ["Wartortle",   [59, 63, 80, 65, 80, 58],   ["water",    "none"],       [],   36,     9],
            9 : ["Blastoise",   [79, 83, 100, 85, 105, 78], ["water",    "none"],       [],   None,   None]
            
            }

moves   = { #"Move Name"     : [power, accuracy, maxPP, dmgType, moveType, contact, hitsAdjacentFoes[0, 1, or 2]],
            "Razor leaf"    : [55, 95, 25, "grass", False, 2]
    }

# ================================================================================================================


class Pokemon: 
    def __init__(self, pokedexInfo:list, mHp:int, hp:int, level:int, status:str=None):
        self._info      = pokedexInfo
        self._maxHp     = mHp
        self._ability   = random.rand(int)
        self.hp         = hp
        self.lvl        = level
        self.status     = status
        self.moves      = [[None, None, None], [None, None, None], [None, None, None], [None, None, None]]
        self.wild       = True
        self.exp        = 0
        
    def get_name(self):
        return self._name
        
    def get_hp(self):
        return self._stats[0]
    
    def get_atk(self):
        return self._stats[1]
    
    def get_spatk(self):
        return self._stats[2]
    
    def get_def(self):
        return self._stats[3]
    
    def get_spdef(self):
        return self._stats[4]
    
    def get_spd(self):
        return self._stats[5]
    
    def add_exp(self):
        return self.exp
    
    
    def attack(self, moveName, target:pokemon):
        moveInfo = moves[moveName]
        power = moveInfo[0]
        accuracy = moveInfo[1]
        dmgType = moveInfo[2]
        moveType = moveInfo[3]
        if moveInfo[3] == self._info[3][0] or moveInfo[3] == self._info[3][1]:
            modifier = 1.5
        
        
        if dmgType == "physical":
            
        elif dmgType== "special":
        
            
        target.take_damage()
    
    def take_damage(self, dmg):
        self.hp -= dmg
    
    def apply_status(self, status):
        self.status = status
        
    def set_move(self, moveName, movePos):
        if movePos > 3:
            ValueError("Invalid move position")
    
    def capture(self):
        self.wild = False
        
        
        
        
    

if __name__ == "__main__":
    # pkmn = pokedex(1, "bulBasAur", [45, 49, 49, 65, 65, 45], "grass", "poison", 16, 2)
    newEntity = Pokemon(pokedex[1], 300, 300, 42)
    
    
    
    print(typeDict.getModifer("", ""))

        
        
        
# HP = floor(0.01 x (2 x Base + IV + floor(0.25 x EV)) x Level) + Level + 10
# Other Stats = (floor(0.01 x (2 x Base + IV + floor(0.25 x EV)) x Level) + 5) x Nature.





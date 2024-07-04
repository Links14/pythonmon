# Trevor Loth
# 6-23-24
# Pokémon and Pokédex class

from math import floor

from pokedex import pokedex
from typeDict import typeChart, getModifier
from moves import moves
import random
import pypokedex as pydex


# ================================================================================================================


class Pokemon:
    
    def __init__(self, entry:int, level:int, status:str=None):
        self._pkmn      = pydex.get(dex=entry)
        self._dexNum    = entry
        self._name      = self._pkmn.name
        self._ability   = random.randint(0,1)
        self._stats     = { "HP"    : self._pkmn.base_stats.hp,
                            "ATK"   : self._pkmn.base_stats.attack,
                            "S.ATK" : self._pkmn.base_stats.sp_atk,
                            "DEF"   : self._pkmn.base_stats.defense,
                            "S.DEF" : self._pkmn.base_stats.sp_def,
                            "SPD"   : self._pkmn.base_stats.speed
                            }
        self._IVs       = { "HP"    : 0,
                            "ATK"   : 0,
                            "S.ATK" : 0,
                            "DEF"   : 0,
                            "S.DEF" : 0,
                            "SPD"   : 0
                            }
        self._EVs       = { "HP"    : 0,
                            "ATK"   : 0,
                            "S.ATK" : 0,
                            "DEF"   : 0,
                            "S.DEF" : 0,
                            "SPD"   : 0
                            }
        self._nature    = { "ATK"   : 1,    # This is a modifier value
                            "S.ATK" : 1,    # The default is 1, but natures should have a single 1.1 value as well as a 0.9 value.
                            "DEF"   : 1,    # Or there should be no changes
                            "S.DEF" : 1,    # Boosted stats should be in red text
                            "SPD"   : 1     # Lowered stats should be in blue text
                            }
        self.lvl        = level
        self.status     = status
        self.maxHp      = floor(0.01 * (2 * self._stats["HP"] + self._IVs["HP"] + floor(0.25 * 1)) * self.lvl) + self.lvl + 10
        self.hp         = self.maxHp
        # HP = floor(0.01 x (2 x Base + IV + floor(0.25 x EV)) x Level) + Level + 10
        #self.moves      = [[None, None, None], [None, None, None], [None, None, None], [None, None, None]] # [MoveName, PP, MaxPP]        
        self.moves      = set_moves(1, level)
        self.wild       = True
        self.exp        = 0
        
    
    def stat_calculator(self, stat:str):
        stat = stat.upper()
        try:
            if stat == "HP":
                return floor(0.01 * (2 * self._stats[stat] + self._IVs[stat] + floor(0.25 * self._EVs[stat])) * self.lvl) + self.lvl + 10
            return (floor(0.01 * (2 * self._stats[stat] + self._IVs[stat] + floor(0.25 * self._EVs[stat])) * self.lvl) + 5) * self._nature[stat]
        except:
            ValueError(f"{stat} is not a valid stat")
        
    def get_name(self):
        return self._name
        
    def get_activeHp(self):
        return self.hp
    
    def get_maxHp(self):
        return self.maxHp
    
    def get_hp(self):
        return self.stat_calculator("hp")
    
    def get_atk(self):
        return self._stats[1] + self._IVs[1]
    
    def get_spatk(self):
        return self._stats[2] + self._IVs[2]
    
    def get_def(self):
        return self._stats[3] + self._IVs[3]
    
    def get_spdef(self):
        return self._stats[4] + self._IVs[4]
    
    def get_spd(self):
        return self._stats[5] + self._IVs[5]
    
    def get_stats(self):
        return self._stats
    
    def get_ivs(self):
        return self._IVs
    
    def get_level(self):
        return self.lvl
    
    def get_move(self, slot):
        return self.moves[slot]
    
    def get_typings(self):
        return pydex.get(dex=self._dexNum).types
    
    def get_sprite(self, side=0):
        # 0 is front, 1 is back
        return pydex.get(dex=self._dexNum).sprites[side]["default"]


    

    def update_maxHp(self):
        self.maxHp = floor(0.01 * (2 * self._pkmn.base_stats.hp + self._IVs[0] + floor(0.25 * 1)) * self.lvl) + self.lvl + 10
        print(self.maxHp)

    def add_exp(self, x):
        self.exp += x
        
    def set_move_pp(self, slot, pp):
        self.moves[slot][1] = pp
        
    def use_move(self, slot):
        self.moves[slot][1] -= 1
    
    def take_damage(self, dmg):
        self.hp -= dmg
    
    def apply_status(self, status, accuracy):
        self.status = status
        
    def set_hp(self, hp):
        self.hp = hp
        
    
    
    def capture(self):
        self.wild = False
        
    def heal(self, val:int=None):
        if val == None:
            self.hp = self._maxHp
            self.status = None
        else:
            if self.hp + val >= self.get_maxhp():
                self.hp = self.get_maxhp()
            else:
                self.hp = val
    
    def set_move(self, moveName, movePos):
        if movePos > 3:
            ValueError("Invalid move position")

    def set_moves_TEST(self, moveSet:list):
        self.moves = moveSet
        

 


def quickSort(array, x=0, y=10000):
    def partition(array, low, high):
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j][0] <= pivot[0]:
                i = i + 1
                temp = array[i]
                array[i] = array[j]
                array[j] = temp
        temp = array[i + 1]
        array[i + 1] = array[high]
        array[high] = temp
        return i + 1 
    
    low  = x
    high = y
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)
    return array

def set_moves(entry, lvl):
    pmoves      = pydex.get(dex=entry).moves["sword-shield"]
    lvlMoves    = []
    moveSet     = []
    for i in pmoves:
        if i[1] == "level-up":
            lvlMoves += [[i[2], i[0]]]
    lvlMoves = quickSort(lvlMoves, 0, len(lvlMoves) - 1)
    
    for i in range(len(lvlMoves) - 1, 0, -1):
        if lvlMoves[i][0] <= lvl:
            moveSet.append([lvlMoves[i][1]])
        if len(moveSet) >= 4:
            break
    return moveSet


#if __name__ == "__main__":




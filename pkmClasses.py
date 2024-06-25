# Trevor Loth
# 6-23-24
# Pokémon and Pokédex class

from math import floor

from pokedex import pokedex
from typeDict import typeChart, getModifer
from moves import moves
import random


# ================================================================================================================


class Pokemon:
    
    def __init__(self, entry:int, mHp:int, hp:int, level:int, status:str=None):
        self._dexNum    = entry
        self._maxHp     = mHp
        self._ability   = random.rand(int)
        self._stats     = pokedex[entry][2]
        self._IVs       = [random.randint(0, 31), random.randint(0, 31), random.randint(0, 31), random.randint(0, 31), random.randint(0, 31), random.randint(0, 31)]
        self.hp         = hp
        self.lvl        = level
        self.status     = status
        self.moves      = [[None, None, None], [None, None, None], [None, None, None], [None, None, None]] # [MoveName, PP, MaxPP]
        self.wild       = True
        self.exp        = 0
        
    def get_name(self):
        return self._name
        
    def get_hp(self):
        return self._stats[0] + self._IVs[0]
    
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
    
    def add_exp(self, x):
        self.exp += x
        
    def get_level(self):
        return self.lvl
    
    def get_move(self, slot):
        return self.moves[slot]
    
    def get_typings(self):
        return pokedex[self._dexNum][2]
    
    def set_move_pp(self, slot, pp):
        self.moves[slot][1] = pp
    
    def take_damage(self, dmg):
        self.hp -= dmg
    
    def apply_status(self, status, accuracy):
        self.status = status
        
    def set_move(self, moveName, movePos):
        if movePos > 3:
            ValueError("Invalid move position")
    
    def capture(self):
        self.wild = False
        
    def heal(self):
        self.hp = self._maxHp
        self.status = None


def set_moves(entry, lvl):
    moveLvls = pokedex[entry][3][1]
    moveSet  = pokedex[entry][3][0]
    index = None
    for i in range(lvl, 0, -1):
        if i in moveLvls:
            index = len(moveLvls) - moveLvls[::-1].index(i)
            break
    if index == None:
        return []
    if index < 4:
        return moveSet[:index]
    return moveSet[index-4: index]




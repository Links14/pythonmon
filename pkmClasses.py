# Trevor Loth
# 6-23-24
# Pokémon and Pokédex class

import typeDict
import random, moves, pokedex


# ================================================================================================================


class Pokemon:
    
    def __init__(self, entry:int, mHp:int, hp:int, level:int, status:str=None):
        self._dexNum    = entry
        self._maxHp     = mHp
        self._ability   = random.rand(int)
        self._stats     = pokedex[entry][2]
        self.hp         = hp
        self.lvl        = level
        self.status     = status
        self.moves      = [[None, None, None], [None, None, None], [None, None, None], [None, None, None]] # [MoveName, PP, MaxPP]
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
        # Varaibles
        moveInfo = moves.moves[moveName]
        power = moveInfo[0]
        accuracy = moveInfo[1]
        dmgType = moveInfo[2]
        moveType = moveInfo[3]
        B = 0
        randVal = random.range(0.85, 1, 0.01)
        
        if dmgType == "physical":
            
        elif dmgType== "special":
        
        else:
            target.apply_status()
            return
        a, d = 
        
        
        
        if moveInfo[3] == self._info[3][0] or moveInfo[3] == self._info[3][1]:
            modifier = 1.5
        
        if dmgType == "physical":
            
        elif dmgType== "special":
        
            
        target.take_damage()
    
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
        
        
        
    

if __name__ == "__main__":
    newEntity = Pokemon(1, 300, 300, 42)
    
    
    
    
    print(typeDict.getModifer("", ""))

        
        

# HP = floor(0.01 x (2 x Base + IV + floor(0.25 x EV)) x Level) + Level + 10
# Other Stats = (floor(0.01 x (2 x Base + IV + floor(0.25 x EV)) x Level) + 5) x Nature.





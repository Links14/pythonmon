# Trevor Loth
# 6-23-24
# Workshopped a pokedex class used for defining and storing values.
# Immediately realized the ridiculously large load that would be imposed by defining an 
    # entire pokedex worth of pokemon everytime the game loads.
# Instead, a dictionary is used with agreed conventions for defining the pokemon outside of the game
# A function to add to the pokedex dictionary may be crated later on

class pokedex:
    def __init__(self, entry:int, name:str, bst:list, t1:str, t2:str="none", evolvl:int=0, evo:int=0):
        self._entry  = entry
        self._name   = name[0].upper() + name[1:].lower()
        self._bst    = bst # Should be a list formatted as [hp, atk, df, spatk, spdf, spd]
        self._type   = [t1.lower(), t2.lower()]
        self._evoLvl = evolvl
        self._evolution = evo

    
    def get_entry(self):
        return self._entry
    
    def get_name(self):
        return self._name
    
    def get_base_stat(self, stat:str):
        if stat == "hp":
            return self._bst[0]
        if stat == "atk":
            return self._bst[1]
        if stat == "df":
            return self._bst[2]
        if stat == "spatk":
            return self._bst[3]
        if stat == "spdf":
            return self._bst[4]
        if stat == "spd":
            return self._bst[5]
        print("Invalid input")
        return None
    
    def get_typings(self):
        return self._type
    
    def get_evolution_lvl(self):
        return self._evoLvl
    
    def get_evolution_entry(self):
        return self._evolution



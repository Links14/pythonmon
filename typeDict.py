# Trevor Loth
# 6-23-24
# Pokémon type chart with a function to get the damage modifier

typeChart = {
    "normal"    : { "normal"    :1,
                    "fire"      :1,
                    "water"     :1,
                    "grass"     :1,
                    "electric"  :1,
                    "ice"       :1,
                    "fighting"  :1,
                    "poison"    :1,
                    "ground"    :1,
                    "flying"    :1,
                    "psychic"   :1,
                    "bug"       :1,
                    "rock"      :0.5,
                    "ghost"     :0,
                    "dragon"    :1,
                    "dark"      :1,
                    "steel"     :0.5,
                    "fairy"     :1
                    },
    "fire"      : { "normal"    :1,
                    "fire"      :.5,
                    "water"     :.5,
                    "grass"     :2,
                    "electric"  :1,
                    "ice"       :2,
                    "fighting"  :1,
                    "poison"    :1,
                    "ground"    :1,
                    "flying"    :1,
                    "psychic"   :1,
                    "bug"       :2,
                    "rock"      :.5,
                    "ghost"     :1,
                    "dragon"    :.5,
                    "dark"      :1,
                    "steel"     :2,
                    "fairy"     :1
                    },
    "water"     : { "normal"    :1,
                    "fire"      :2,
                    "water"     :.5,
                    "grass"     :.5,
                    "electric"  :1,
                    "ice"       :1,
                    "fighting"  :1,
                    "poison"    :1,
                    "ground"    :2,
                    "flying"    :1,
                    "psychic"   :1,
                    "bug"       :1,
                    "rock"      :2,
                    "ghost"     :1,
                    "dragon"    :.5,
                    "dark"      :1,
                    "steel"     :1,
                    "fairy"     :1
                    },
    "grass"     : { "normal"    :1,
                    "fire"      :.5,
                    "water"     :2,
                    "grass"     :.5,
                    "electric"  :1,
                    "ice"       :1,
                    "fighting"  :1,
                    "poison"    :.5,
                    "ground"    :2,
                    "flying"    :.5,
                    "psychic"   :1,
                    "bug"       :.5,
                    "rock"      :2,
                    "ghost"     :1,
                    "dragon"    :.5,
                    "dark"      :1,
                    "steel"     :.5,
                    "fairy"     :1
                    },
    "electric"  : { "normal"    :1,
                    "fire"      :1,
                    "water"     :2,
                    "grass"     :.5,
                    "electric"  :.5,
                    "ice"       :1,
                    "fighting"  :1,
                    "poison"    :1,
                    "ground"    :0,
                    "flying"    :2,
                    "psychic"   :1,
                    "bug"       :1,
                    "rock"      :1,
                    "ghost"     :1,
                    "dragon"    :.5,
                    "dark"      :1,
                    "steel"     :1,
                    "fairy"     :1
                    },
    "ice"       : { "normal"    :1,
                    "fire"      :.5,
                    "water"     :.5,
                    "grass"     :2,
                    "electric"  :1,
                    "ice"       :.5,
                    "fighting"  :1,
                    "poison"    :1,
                    "ground"    :2,
                    "flying"    :2,
                    "psychic"   :1,
                    "bug"       :1,
                    "rock"      :1,
                    "ghost"     :1,
                    "dragon"    :2,
                    "dark"      :1,
                    "steel"     :.5,
                    "fairy"     :1
                    },
    "fighting"  : { "normal"    :2,
                    "fire"      :1,
                    "water"     :1,
                    "grass"     :1,
                    "electric"  :1,
                    "ice"       :2,
                    "fighting"  :1,
                    "poison"    :.5,
                    "ground"    :1,
                    "flying"    :.5,
                    "psychic"   :.5,
                    "bug"       :.5,
                    "rock"      :2,
                    "ghost"     :0,
                    "dragon"    :1,
                    "dark"      :2,
                    "steel"     :2,
                    "fairy"     :.5
                    },
    "poison"    : { "normal"    :1,
                    "fire"      :1,
                    "water"     :1,
                    "grass"     :2,
                    "electric"  :1,
                    "ice"       :1,
                    "fighting"  :1,
                    "poison"    :.5,
                    "ground"    :.5,
                    "flying"    :1,
                    "psychic"   :1,
                    "bug"       :1,
                    "rock"      :.5,
                    "ghost"     :.5,
                    "dragon"    :1,
                    "dark"      :1,
                    "steel"     :0,
                    "fairy"     :2
                    },
    "ground"    : { "normal"    :1,
                    "fire"      :2,
                    "water"     :1,
                    "grass"     :.5,
                    "electric"  :2,
                    "ice"       :1,
                    "fighting"  :1,
                    "poison"    :2,
                    "ground"    :1,
                    "flying"    :0,
                    "psychic"   :1,
                    "bug"       :.5,
                    "rock"      :2,
                    "ghost"     :1,
                    "dragon"    :1,
                    "dark"      :1,
                    "steel"     :2,
                    "fairy"     :1
                    },
    "flying"    : { "normal"    :1,
                    "fire"      :1,
                    "water"     :1,
                    "grass"     :2,
                    "electric"  :.5,
                    "ice"       :1,
                    "fighting"  :2,
                    "poison"    :1,
                    "ground"    :1,
                    "flying"    :1,
                    "psychic"   :1,
                    "bug"       :2,
                    "rock"      :.5,
                    "ghost"     :1,
                    "dragon"    :1,
                    "dark"      :1,
                    "steel"     :.5,
                    "fairy"     :1
                    },
    "psychic"   : { "normal"    :1,
                    "fire"      :1,
                    "water"     :1,
                    "grass"     :1,
                    "electric"  :1,
                    "ice"       :1,
                    "fighting"  :2,
                    "poison"    :2,
                    "ground"    :1,
                    "flying"    :1,
                    "psychic"   :.5,
                    "bug"       :1,
                    "rock"      :1,
                    "ghost"     :1,
                    "dragon"    :1,
                    "dark"      :0,
                    "steel"     :.5,
                    "fairy"     :1
                    },
    "bug"       : { "normal"    :1,
                    "fire"      :.5,
                    "water"     :1,
                    "grass"     :2,
                    "electric"  :1,
                    "ice"       :1,
                    "fighting"  :.5,
                    "poison"    :.5,
                    "ground"    :1,
                    "flying"    :.5,
                    "psychic"   :2,
                    "bug"       :1,
                    "rock"      :1,
                    "ghost"     :.5,
                    "dragon"    :1,
                    "dark"      :2,
                    "steel"     :.5,
                    "fairy"     :.5
                    },
    "rock"      : { "normal"    :1,
                    "fire"      :2,
                    "water"     :1,
                    "grass"     :1,
                    "electric"  :1,
                    "ice"       :2,
                    "fighting"  :.5,
                    "poison"    :1,
                    "ground"    :.5,
                    "flying"    :2,
                    "psychic"   :1,
                    "bug"       :2,
                    "rock"      :1,
                    "ghost"     :1,
                    "dragon"    :1,
                    "dark"      :1,
                    "steel"     :.5,
                    "fairy"     :1
                    },
    "ghost"     : { "normal"    :0,
                    "fire"      :1,
                    "water"     :1,
                    "grass"     :1,
                    "electric"  :1,
                    "ice"       :1,
                    "fighting"  :1,
                    "poison"    :1,
                    "ground"    :1,
                    "flying"    :1,
                    "psychic"   :2,
                    "bug"       :1,
                    "rock"      :1,
                    "ghost"     :2,
                    "dragon"    :1,
                    "dark"      :.5,
                    "steel"     :1,
                    "fairy"     :1
                    },
    "dragon"    : { "normal"    :1,
                    "fire"      :1,
                    "water"     :1,
                    "grass"     :1,
                    "electric"  :1,
                    "ice"       :1,
                    "fighting"  :1,
                    "poison"    :1,
                    "ground"    :1,
                    "flying"    :1,
                    "psychic"   :1,
                    "bug"       :1,
                    "rock"      :1,
                    "ghost"     :1,
                    "dragon"    :2,
                    "dark"      :1,
                    "steel"     :.5,
                    "fairy"     :0
                    },
    "dark"      : { "normal"    :1,
                    "fire"      :1,
                    "water"     :1,
                    "grass"     :1,
                    "electric"  :1,
                    "ice"       :1,
                    "fighting"  :.5,
                    "poison"    :1,
                    "ground"    :1,
                    "flying"    :1,
                    "psychic"   :2,
                    "bug"       :1,
                    "rock"      :1,
                    "ghost"     :2,
                    "dragon"    :1,
                    "dark"      :.5,
                    "steel"     :1,
                    "fairy"     :.5
                    },
    "steel"     : { "normal"    :1,
                    "fire"      :.5,
                    "water"     :.5,
                    "grass"     :1,
                    "electric"  :.5,
                    "ice"       :2,
                    "fighting"  :1,
                    "poison"    :1,
                    "ground"    :1,
                    "flying"    :1,
                    "psychic"   :1,
                    "bug"       :1,
                    "rock"      :2,
                    "ghost"     :1,
                    "dragon"    :1,
                    "dark"      :1,
                    "steel"     :.5,
                    "fairy"     :2
                    },
    "fairy"     : { "normal"    :1,
                    "fire"      :.5,
                    "water"     :1,
                    "grass"     :1,
                    "electric"  :1,
                    "ice"       :1,
                    "fighting"  :2,
                    "poison"    :.5,
                    "ground"    :1,
                    "flying"    :1,
                    "psychic"   :1,
                    "bug"       :1,
                    "rock"      :1,
                    "ghost"     :1,
                    "dragon"    :2,
                    "dark"      :2,
                    "steel"     :.5,
                    "fairy"     :1
                    },
    "none"    : { "normal"      :1,
                    "fire"      :1,
                    "water"     :1,
                    "grass"     :1,
                    "electric"  :1,
                    "ice"       :1,
                    "fighting"  :1,
                    "poison"    :1,
                    "ground"    :1,
                    "flying"    :1,
                    "psychic"   :1,
                    "bug"       :1,
                    "rock"      :1,
                    "ghost"     :1,
                    "dragon"    :1,
                    "dark"      :1,
                    "steel"     :1,
                    "fairy"     :1
                    }
            }

def getModifier(atk, df:list):
    atk = atk.lower()
    df1 = df[0].lower()
    dmg1 = typeChart[atk][df1]
    try:
        df2 = df[1].lower()
        dmg2 = typeChart[atk][df2]
        dmg = dmg1 * dmg2
    except:
        dmg = dmg1
    
    if dmg == 0:
        print("does not effect the enemy pokemon")
    elif dmg == 0.25 or dmg == 0.5:
        print("was not very effective")
    elif dmg == 2 or dmg == 4:
        print("was very effective")
    
    return dmg






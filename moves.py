# Trevor Loth
# 6-23-24
# List of moves

moves   = { #"Move Name"    : [power, accuracy, maxPP, dmgType, moveType, status, contact, hitsAdjacentFoes],
            "razor-leaf"    : [55,  95,     25, "physical", "grass",    None,       False, True],
            "poison-powder" : [0,   75,     35, "status",   "poison",   "poison",   False, False],
            "growl"         : [0,   100,    40, "status",   "normal",   None,       False, True],  # Lowers attack by 1 stage
            "tackle"        : [40,  100,    35, "physical", "normal",   None,       True,  False],
            "vine-whip"     : [45,  100,    25, "physical", "grass",    None,       True,  False],
            "growth"        : [0,   None,   20, "status",   "normal",   None,       False, False], # increase the atk and spatk by one each, by two if in harsh sunlight
            "leech-seed"    : [0,   90,     20, "status",   "grass",    None,       False, False],
            "sleep-powder"  : [0,   75,     15, "status",   "grass",   "sleep",     False, False],
            "seed-bomb"     : [80,  100,    15, "physical", "grass",    None,       False, False],
            "take-down"     : [90,  85,     20, "physical", "normal",   None,       True,  False],
            "sweet-scent"   : [0,   100,    20, "status",   "normal",   None,       False, True],
            "synthesis"     : [0,   None,   5,  "status",   "grass",    None,       False, False],
            "worry-seed"    : [0,   100,    10, "status",   "grass",    None,       False, False],
            "power-whip"    : [120, 85,     10, "physical", "grass",    None,       True,  False],
            "solar-beam"    : [120, 100,    10, "special",  "grass",    None,       False, False]
           
    }
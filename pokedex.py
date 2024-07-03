# Trevor Loth
# 6-23-24
# Pokémon type chart with a function to get the damage modifier


# DEPRECIATED
# USED LIBRARY "pypokedex" INSTEAD

"""
This package (pypokedex) only provides one function through the public API—get. It can be used as follows:

import pypokedex

pokemon = pypokedex.get(dex=DEX)  # DEX must be a valid _national_ pokedex
                                  # number
pokemon2 = pypokedex.get(name=NAME)  # NAME must be a valid name of a pokemon
In addition to the above function, the following classes are provided as part of the public API:

Pokemon (returned by get),
BaseStats,
Ability,
Sprites,
and Move
Note that these classes shouldn't be initialized through client code; their purpose is mainly for type annotations.

Possible Exceptions
A TypeError will be raised if the wrong number of arguments or the wrong type of arguments are passed.
A PyPokedexHTTPError will be raised with an HTTP code of 404 if the Pokemon requested is not found. Note: The name parameter to get is case-insensitive.
A PyPokedexHTTPError will be raised with the proper HTTP code if another type of HTTP error occurs.
A PyPokedexError will be raised if a requests exception occurs (with the exception of requests.exceptions.HTTPError, handled in the previous two bullet points).
A PyPokedexError will be raised if data is missing when parsing the returned JSON from PokeAPI (usually this indicates an API change).
Once a valid pypokedex.pokemon.Pokemon object is returned, the following members are provided for its consumption:

Member Variables
dex (int): Contains the national Pokedex number of the current Pokemon.
name (str): Contains the name of the current Pokemon.
height (int): Contains the height of the current Pokemon in decimeters (see veekun/pokedex#249).
weight (int): Contains the weight of the current Pokemon in hectograms (see veekun/pokedex#249).
base_experience (intt): Contains the base experience yield of the current Pokemon.
types (List[str]): Contains a list of strings with the name of the current Pokemon's types.
abilities (List[Ability]): Contains a list of named tuples called Ability. Each Ability has the following members:
name (str): The name of the current ability.
is_hidden (bool): Whether the current ability is a hidden ability or not.
base_stats (BaseStats): Contains a named tuple with the current Pokemon's base stats stored as follows (all ints):
hp: The base HP of the current Pokemon.
attack: The base attack of the current Pokemon.
defense: The base defense of the current Pokemon.
sp_atk: The base special attack of the current Pokemon.
sp_def: The base special defense of the current Pokemon.
speed: The base speed of the current Pokemon.
moves (DefaultDict[str, List[Move]]): Contains a dictionary of game names (according to PokeAPI) to a list of named tuples called Move representing the moves the current Pokemon learns in the respective game. The Move named tuple contains the following members:
name (str): The name of the current move.
learn_method (str): The method the current Pokemon uses to learn the current move (according to PokeAPI).
level (int): The level the current Pokemon learns the current move if learn_method is level-up, None otherwise.
sprites (Sprites): Contains two dictionaries, front and back representing the respective sprites of the current Pokemon. The keys in the dictionary are Pokeapi sprite keys without the direction prefix (e.g back_default is just default in the back dictionary).
other_sprites (Dict[str, Sprites]): Contains a mapping of sprite groups to sprites (sprites are stored in the same way as the sprites instance variable.
version_sprites (Dict[str, Dict[str, Sprites]]): Contains a mapping of generations to games to sprites. Note that like the API itself, keys are included for all generations and games, despite the fact that those Pokemon may not exist in said generation or game. e.g pypokedex.get(name='garchomp') would include keys for generation 1 through 3, even though it was introduced in generation 4.
Member Functions
def exists_in(self, game: str) -> bool: Method to check whether the current Pokemon exists in a specific game.
def learns(self, move_name: str, game: str) -> bool: Method to check whether the current Pokemon learns a specific move in a specific game.
def get_descriptions(self, language="en") -> Dict[str, str]: Method to returns all the descriptions of the current Pokemon for the specified language (en by default). Note: This function only returns the descriptions as a dictionary. It doesn't store them anywhere on the Pokemon object. This was done since the descriptions are fetched from a separate API endpoint.
def __str__(self) -> str: Method to get a string represenation of the current Pokemon. This string is of the form: Pokemon(dex={self.dex}, name='{self.name}').
__eq__, __lt__, __gt__, __le__, __ge__: Methods that implement various comparison operators for Pokemon objects in terms of their Pokedex number.
Possible Exceptions
learns will raise a PyPokedexError if the current Pokemon does not exist in the game specified.
"""







            # : ["",   [, , , , , ],   "",     "",     ,   ]
pokedex = { # EntryNum:int : ["name", [hp, atk, df, spatk, spdf, spd], ["type1", "type2"], [[moves], [correspondinglevel]], evoLVL, evolutionEntry]
            1 : ["Bulbasaur",   [45, 49, 49, 65, 65, 45],   ["grass",    "poison"],    {1 : ["growl", "tackle"],
                                                                                        3 : ["vine whip"],
                                                                                        6 : ["growth"],
                                                                                        9 : ["leech seed"],
                                                                                        12 : ["razor leaf"],
                                                                                        15 : ["sleep powder"],
                                                                                        18 : ["seed bomb"],
                                                                                        21 : ["take down"],
                                                                                        24 : ["sweet scent"],
                                                                                        27 : ["synthesis"],
                                                                                        30 : ["worry seed"],
                                                                                        33 : ["power whip"],
                                                                                        36 : ["solar beam"],
                                                                                        },   16,     2],
            2 : ["Ivysaur",     [60, 62, 63, 80, 80, 60],   ["grass",    "poison"],     {},   32,     3],
            3 : ["Venosaur",    [80, 82, 83, 100, 100, 80], ["grass",    "poison"],     {},   None,   None],
            4 : ["Charmander",  [39, 52, 43, 60, 50, 65],   ["fire",     "none"],       {},   16,     5],
            5 : ["Charmeleon",  [58, 64, 58, 80, 65, 80],   ["fire",     "none"],       {},   36,     6],
            6 : ["Charizard",   [78, 84, 78, 109, 85, 100], ["fire",     "flying"],     {},   None,   None],
            7 : ["Squirtle",    [44, 48, 65, 50, 64, 43],   ["water",    "none"],       {},   16,     8],
            8 : ["Wartortle",   [59, 63, 80, 65, 80, 58],   ["water",    "none"],       {},   36,     9],
            9 : ["Blastoise",   [79, 83, 100, 85, 105, 78], ["water",    "none"],       {},   None,   None]
            
            }







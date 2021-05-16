from random import randrange
from names_list import *
from races import *

dictionary = {"Lunadin": {"race": "Elf", "exp": 286, "coins": 125, "dungeons_cleared": 20, "kills": 119},
 "Kronk": {"coins": 0, "dungeons_cleared": 1, "kills": 2},
"Malakovich": {"coins": 54, "dungeons_cleared": 1, "kills": 7}}

hero = "Lunadin"
def get_race(hero, alist):
    for race in alist:
        if dictionary[hero]["race"] == race.__name__:
            return race

test = get_race(hero, available_race_for_hero_list)()
print(test)


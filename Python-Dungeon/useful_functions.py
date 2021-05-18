from races_inher import *
from names_list import *
from time import sleep


def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            break
        except:
            print("Wrong input!")
            continue
    return value


# def get_name(race):
#     if isinstance(race, Orc):
#         random_name = orcs[randrange(0, len(orcs))] + " the Orc"
#         return random_name
#     elif isinstance(race, Goblin):
#         random_name = ("Goblin " + goblins[randrange(0, len(goblins))])
#         return random_name


def get_menu_choice():  # Enter Market

    print("Welcome to Python-Dungeon!")
    sleep(1)

    choice = get_int("""
    1 - Enter Dungeon
    2 - Print stats
    3 - Exit
    """)
    return choice


def update_stats(stats_dictionary, hero, char, no_dungeons, kills):
    stats_dictionary[hero]["exp"] += char.exp
    stats_dictionary[hero]["coins"] += char.currency
    stats_dictionary[hero]["dungeons_cleared"] += no_dungeons
    stats_dictionary[hero]["kills"] += kills


def check_account(hero, stats_dictionary):
    if not stats_dictionary:
        stats_dictionary = {}
    else:
        for key in list(stats_dictionary.keys()):
            if key == hero:
                sleep(1)
                print(f"\nDelighted to have you back {hero}.\n")
                break
        else:
            stats_dictionary[hero] = {}
            print(f"Available races\n"+"-"*15)
            for idx, x in enumerate(hero_races):
                print(f"{idx +1}: {x}")
            choice = get_int("Choose your race: ") - 1
            race_chosen = hero_races[choice]
            stats_dictionary[hero]["race"] = race_chosen
            stats_dictionary[hero]["exp"] = 0
            stats_dictionary[hero]["coins"] = 0
            stats_dictionary[hero]["dungeons_cleared"] = 0
            stats_dictionary[hero]["kills"] = 0
            sleep(1)
            print(f"\nFirst time {hero}? Good luck.\n")


def set_player(hero, stats_dictionary):
    for race in hero_races:
        if stats_dictionary[hero]["race"] == race:
            return eval(race + "(hero)")

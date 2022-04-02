from os import X_OK
from races import *
from list_names import *
from list_items import items
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


def get_menu_choice():  # Enter Market

    print("Welcome to Python-Dungeon!")
    sleep(1)

    choice = get_int("""
    1 - Enter Dungeon
    2 - Enter Market
    3 - Print stats
    4 - Exit
    """)
    return choice


def update_stats(stats_dictionary, hero, char, no_dungeons, kills):
    s = stats_dictionary[hero]
    s["level"] = char.level
    s["exp"] = char.exp
    s["exp_for_level"] = char.exp_for_level
    s["coins"] = char.currency
    s['inventory'] = char.inventory
    s["dungeons_cleared"] += no_dungeons
    s["kills"] += kills
    for i, owned_item in reversed(list(enumerate(s['inventory']))): # CANT ITERATE TWICE. WHY?
        x = 0
        print(items)
        while x < len(items):
            if (owned_item == items[x]['name']) and (items[x]['type'] == 'one_use'):
                s['inventory'].pop(i)
                print(f"{owned_item} has expired so you dropped it.")
            x += 1
                


def check_account(hero, stats_dictionary):

    for key in list(stats_dictionary.keys()):
        if key == hero:
            sleep(1)
            print(f"\nWelcome back {hero}.\n")
            break
    else:
        stats_dictionary[hero] = {}
        print("Available races\n"+"-"*15)
        for idx, x in enumerate(hero_races):
            print(f"{idx +1}: {x}")
        choice = get_int("Choose your race: ") - 1
        race_chosen = hero_races[choice]
        stats_dictionary[hero]["race"] = race_chosen
        stats_dictionary[hero]["level"] = 1
        stats_dictionary[hero]["exp"] = 0
        stats_dictionary[hero]["exp_for_level"] = 100
        stats_dictionary[hero]["coins"] = 0
        stats_dictionary[hero]["inventory"] = []
        stats_dictionary[hero]["dungeons_cleared"] = 0
        stats_dictionary[hero]["kills"] = 0
        sleep(1)
        print(f"\nFirst time {hero}? Good luck.\n")

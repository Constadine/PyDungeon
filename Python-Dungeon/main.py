import json
from random import randrange, seed
from datetime import datetime
from handle_battle import Battle
from handle_explore import Explore
from handle_market import Market
from useful_functions import *


def main():
    # seed(datetime.now())
    try:
        with open("player_stats.json") as f:
            player_stats = json.load(f)
    except FileNotFoundError:
        player_stats = {}

    hero_name = input("Name your hero: ")
    check_account(hero_name, player_stats)
    sleep(1)

    while True:

        menu_choice = get_menu_choice()
        me = eval(player_stats[hero_name]["race"] + "()")
        me.load_char(hero_name, player_stats)
        if menu_choice == 1:
            kills = 0
            dungeon_clear = 0

            me.set_stats()
            turn = 0
            random_size_dungeon = 1
# randrange(5, 11)
            exploring = Explore(me)
            while True:

                turn += 1
                # random_race = npc_races[randrange(0, len(npc_races))]

                enemy = eval(npc_races[randrange(0, len(npc_races))])

                print(f"\nTurn {turn}")
                battle_event = Battle(me, enemy)
                kills += battle_event.fight()

                if turn == random_size_dungeon:
                    print("You've captured this dungeon!")
                    dungeon_clear += 1
                    update_stats(player_stats, hero_name,
                                 me, dungeon_clear, kills)
                    with open("player_stats.json", "w") as f:
                        json.dump(player_stats, f)
                    break
                elif me.is_dead():
                    print("You died.")
                    update_stats(player_stats, hero_name,
                                 me, dungeon_clear, kills)
                    with open("player_stats.json", "w") as f:
                        json.dump(player_stats, f)
                    break

                exploring.explore(me)

        elif menu_choice == 2:
            market_place = Market(me)
            market_place.use_market(me)


        elif menu_choice == 3:
            print(f"{hero_name}'s stats: ")
            for key, value in player_stats[hero_name].items():
                print(f"{key}: {value}".capitalize().replace("_", ' '))

        elif menu_choice == 4:
            with open("player_stats.json", "w") as f:
                json.dump(player_stats, f)
            print("May the light never find you..")
            break


main()

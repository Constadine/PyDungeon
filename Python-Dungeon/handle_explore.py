from random import randrange
from useful_functions import get_int
from time import sleep

events = {
    "exp": ["Sliced a tree to pieces.", "Your chest is destroyed."],
    "heal": ["You sit near a magical waterfall.", "You rest near a fire."],
    "loot": ["You found something behind a rock..", "You opened an old chest.."]

}


class Explore:
    def __init__(self, character) -> None:
        self.name = character.name
        self.health = character.health
        self.currency = character.currency
        self.heal_chances = 5

    def explore(self, character):

        while True:
            sleep(1)
            choice = get_int("""
            1 - Train..
            2 - Find place to heal..
            3 - Search for treasure..\n""")
            sleep(1)
            if choice == 1:   
                random_event = randrange(0, len(events["exp"]))
                print(events["exp"][random_event])
                exp_gained = randrange(5, 21)
                character.exp += exp_gained
                sleep(1)
                print(f"You've gained {exp_gained} exp!")
                sleep(1)
                break
            elif choice == 2:
                if character.health == character.maxhealth:
                    print("You are at max health!")
                    continue
                else:
                    if self.heal_chances > 0:
                        random_event = randrange(0, len(events["heal"]))
                        print(events["heal"][random_event])
                        heal = randrange(5, 8)
                        character.health += heal
                        if character.health > character.maxhealth:
                            character.health = character.maxhealth
                        sleep(1)
                        print(f"You've healed for {heal} hp.")
                        sleep(1)
                        self.heal_chances -= 1
                        print(f"You have {self.heal_chances} more heals.")
                        break
                    else:
                        print("You can't heal anymore..")
                        continue
            elif choice == 3:
                random_event = randrange(0, len(events["loot"]))
                chance_for_loot = randrange(0, 3)
                if chance_for_loot == 1:
                    print(events["loot"][random_event])
                    sleep(1)
                    loot_type = randrange(0, 11)
                    if loot_type < 2:
                        print("You've found a weapon.")
                        sleep(1)
                    elif loot_type > 7:
                        print("You've found a potion!")
                        self.heal_chances += 1
                        sleep(1)
                    else:
                        random_coins = randrange(10, 41)
                        character.currency += random_coins
                        print(
                            f"Shiny coins.. You've gained {random_coins} coins!")
                        sleep(1)
                    break
                else:
                    print("You've found nothing..")
                    sleep(1)
                    break

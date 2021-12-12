from random import randrange
from time import sleep

from list_names import *
from characters import Character, Npc


class Elf(Character):

    def __init__(self):
        super().__init__()
        self.max_health = 98
        self.health = self.max_health
        self.max_mana = 98
        self.mana = self.max_mana
        self.damage = (12, 17)
        self.crit_damage = 3
        self.crit_chance = 7
        self.speed = 3
        self.hp_regeneration = 2
        self.mp_regeneration = 2
        self.skills = [self.wind_slice, self.poison_arrow]


    def wind_slice(self, *args, **kwargs):
        mana_cost = 30
        if self.mana >= mana_cost:

            self.mana -= mana_cost
            first_hit, crit_check = self.attack(1, 5)
            second_hit, crit_check = self.attack(0.5, 0)
            total_damage = first_hit + second_hit
            sleep(1)
            print(f"{self.name} striked twice using Wind Strike.")
            sleep(1)
            print(
                f"First hit dealt {first_hit} and a wave of air cut for {second_hit} damage")
            sleep(1)

            return total_damage
        else:
            print(f"Not enough mana! {self.mana}/{mana_cost}")
            return False

    def poison_arrow(self, enemy):
        mana_cost = 20
        if self.mana >= mana_cost:

            self.mana -= mana_cost
            enemy.afflictions.append("Poison")
        else:
            print(f"Not enough mana! {self.mana}/{mana_cost}")
            return False

    def __len__(self):
        return len(self.skills)

    def __getitem__(self, skill):
        return self.skills[skill]



class Mage(Character):

    def __init__(self):
        super().__init__()

        self.max_health = 79
        self.health = self.max_health
        self.max_mana = 196
        self.mana = self.max_mana
        self.damage = (10, 13)
        self.crit_damage = 4
        self.crit_chance = 9
        self.speed = 2
        self.hp_regeneration = 1
        self.mp_regeneration = 4

    def set_stats(self):
        return super().set_stats(1, 4)

    def level_up(self):
        return super().level_up(1, 4)


class Goblin(Npc):
    def __init__(self):
        super().__init__()

        self.name = "Goblin " + goblins[randrange(0, len(goblins))]
        self.health = 15
        self.max_health = self.health
        self.mana = 0
        self.damage = 3
        self.crit_chance = 10
        self.crit_damage = 0
        self.speed = 1


class Orc(Npc):
    def __init__(self) -> None:
        super().__init__()

        self.name = orcs[randrange(0, len(orcs))] + " the Orc"
        self.health = 30
        self.max_health = self.health
        self.mana = 0
        self.damage = 8
        self.crit_chance = 9
        self.crit_damage = 5
        self.speed = 1


# implement this on handle battle

afflictions_dict = {
    "Poison": {"damage": 2, "duration": 3}
}

def check_afflictions(char,afflictions_dict, rounds):
    if "Poison" in char.afflictions:
        duration = afflictions_dict["Poison"]["duration"]
        
        char.health -= afflictions_dict["Poison"]["damage"]
        print(char.health)
        duration -= rounds
        print(duration)
        if duration == 0:
            char.afflictions.remove("Poison")
            print('popped')
            return True
npc_races = ['Orc()', 'Goblin()']
hero_races = ['Elf', 'Mage']

# legolas = Elf()
# bob = Orc()
# rounds = 0
# legolas.poison_arrow(bob)   
# while True:


#     end = check_afflictions(bob, afflictions_dict, rounds)
#     rounds += 1
#     input("enter")
#     if end: break







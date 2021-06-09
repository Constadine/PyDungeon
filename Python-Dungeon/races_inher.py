from random import randrange
from names_list import *
from characters import Character, Npc


class Elf(Character):

    def __init__(self):
        super().__init__()
        self.max_health = 98
        self.health = self.max_health
        self.max_mana = 98
        self.mana = self.max_mana
        self.damage = 12
        self.crit_damage = 3
        self.crit_chance = 7
        self.speed = 3
        self.hp_regeneration = 2
        self.mp_regeneration = 2


class Mage(Character):

    def __init__(self):
        super().__init__()

        self.max_health = 79
        self.health = self.max_health
        self.max_mana = 196
        self.mana = self.max_mana
        self.damage = 14
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


npc_races = ['Orc()', 'Goblin()']
hero_races = ['Elf', 'Mage']

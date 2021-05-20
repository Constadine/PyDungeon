from random import randrange
from names_list import *
from characters import Character, Npc


class Elf(Character):

    def __init__(self):
        Character.__init__(self)
        self.maxhealth = 100
        self.health = self.maxhealth
        self.mana = 100
        self.damage = 12
        self.crit_damage = 3
        self.crit_chance = 7
        self.speed = 3
        self.regeneration = 2


class Mage(Character):

    def __init__(self):
        Character.__init__(self)

        self.maxhealth = 80
        self.health = self.maxhealth
        self.mana = 200
        self.damage = 14
        self.crit_damage = 4
        self.crit_chance = 9
        self.speed = 2
        self.regeneration = 1


class Goblin(Npc):
    def __init__(self,):
        Npc.__init__(self)

        self.name = "Goblin " + goblins[randrange(0, len(goblins))]
        self.health = 15
        self.maxhealth = self.health
        self.mana = 0
        self.damage = 3
        self.crit_chance = 10
        self.crit_damage = 0
        self.speed = 1


class Orc(Npc):
    def __init__(self) -> None:
        Npc.__init__(self)

        self.name = orcs[randrange(0, len(orcs))] + " the Orc"
        self.health = 30
        self.maxhealth = self.health
        self.mana = 0
        self.damage = 8
        self.crit_chance = 9
        self.crit_damage = 5
        self.speed = 1


npc_races = ['Orc()', 'Goblin()']
hero_races = ['Elf', 'Mage']

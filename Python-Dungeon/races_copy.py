from random import randrange
from names_list import *
from characters import Npc


class Elf:
    def __init__(self):
        self.maxhealth = 100
        self.health = self.maxhealth
        self.mana = 100
        self.damage = 12
        self.crit_damage = 3
        self.crit_chance = 7
        self.speed = 3


class Goblin(Npc):
    def __init__(self):
        Npc.__init__(self)

    def __init__(self, health=10):
        self.name = "Goblin " + goblins[randrange(0, len(goblins))]
        self.health = health
        self.mana = 0
        self.damage = 3
        self.crit_chance = 10
        self.crit_damage = 0
        self.speed = 1


class Orc(Npc):
    def __init__(self) -> None:
        Npc.__init__(self)
    
    def __init__(self, health=30):
        self.name = orcs[randrange(0, len(orcs))] + " the Orc"
        self.health = health
        self.mana = 0
        self.damage = 8
        self.crit_chance = 9
        self.crit_damage = 5
        self.speed = 1


available_race_for_mobs_list = [Orc, Goblin]

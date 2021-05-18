from names_list import *

# Spell list!!


class Elf:
    def __init__(self):
        self.maxhealth = 100
        self.health = self.maxhealth
        self.mana = 100
        self.damage = 12
        self.crit_damage = 3
        self.crit_chance = 7
        self.speed = 3
        self.regeneration = 2


class Mage:
    def __init__(self) -> None:
        self.maxhealth = 80
        self.health = self.maxhealth
        self.mana = 200
        self.damage = 14
        self.crit_damage = 4
        self.crit_chance = 9
        self.speed = 3


class Goblin:
    def __init__(self, health=10):
        self.health = health
        self.mana = 0
        self.damage = 3
        self.crit_chance = 10
        self.crit_damage = 0
        self.speed = 1


class Orc:
    def __init__(self, health=30):
        self.name = []
        self.health = health
        self.mana = 0
        self.damage = 8
        self.crit_chance = 9
        self.crit_damage = 5
        self.speed = 1


npc_races = [Orc, Goblin]
hero_races = [Elf, Mage]

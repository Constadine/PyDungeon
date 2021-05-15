from random import randrange


class Character:  # add exp and levels. Health and damage will increase per level
    def __init__(self, name, race):
        self.name = name
        self.race = race
        self.exp = 0  # earn exp when killing enemies, clearing dungeon and exploring
        # Have a chance to loot when exploring. Create market to buy permanent buffs
        self.currency = 0
        self.maxhealth = race.maxhealth
        self.health = race.health
        self.mana = race.mana
        self.speed = race.speed
        self.damage = race.damage
        self.crit_damage = race.crit_damage
        self.crit_chance = race.crit_chance
        self.regeneration = race.regeneration

    def is_dead(self):
        return self.health <= 0

    def attack(self):
        crit_roll = randrange(0, 11)
        if crit_roll > self.race.crit_chance:
            return self.race.damage + randrange(1, 3) + self.race.crit_damage, True
        else:
            return self.race.damage + randrange(1, 3), False

    def regen(self):
        self.health = self.health + self.regeneration if self.health + \
            self.regeneration <= self.maxhealth else self.maxhealth


class Npc:
    def __init__(self, name, race):
        self.name = name
        self.race = race
        self.health = race.health
        self.mana = race.mana
        self.damage = race.damage
        self.crit_chance = race.crit_chance
        self.crit_damage = race.crit_damage
        self.speed = race.speed

    def is_dead(self):
        return self.health <= 0

    def attack(self):
        crit_roll = randrange(0, 11)
        if crit_roll > self.crit_chance:
            return self.damage + randrange(1, 3) + self.crit_damage, True
        else:
            return self.damage + randrange(1, 3), False

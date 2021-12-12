from random import randrange
from time import sleep
from abc import ABC


class Character(ABC):  # add exp and levels. Health and damage will increase per level
    def __init__(self):
        self.name = ""
        self.currency = 0
        self.exp = 0
        self.exp_for_level = 100
        self.level = 1
        self.potions = 5
        self.inventory = []
        self.afflictions = []
        self.buffs = []
        
    def item_bonuses(self):
        if "Potion Holder" in self.inventory:
            self.potions += 1
        if "Vigor Root" in self.inventory:
            self.max_health += 20 
        

    def load_char(self, name, player_stats):
        for key in player_stats.keys():
            if key == name:
                self.name = key
                self.level = player_stats[name]["level"]
                self.exp_for_level = player_stats[name]["exp_for_level"]
                self.exp = player_stats[name]["exp"]
                self.currency = player_stats[name]["coins"]
                self.inventory = player_stats[name]["inventory"]

                

    def set_stats(self, health_amount=2, mana_amount=2):  # In races.py can be specialized
        self.item_bonuses()
        self.max_health += health_amount * self.level
        self.health = self.max_health
        self.max_mana += mana_amount * self.level
        self.mana = self.max_mana


    def level_up(self, health_amount=2, mana_amount=2):
        if self.exp >= self.exp_for_level:
            for _ in range(self.exp // self.exp_for_level):
                self.level += 1
                self.max_health = self.max_health + health_amount
                self.max_mana = self.max_mana + mana_amount
                print(f"You leveled up! LvL {self.level}")
                sleep(1)
                print(
                    f"Your max health increased to {self.max_health} and your max mana to {self.max_mana}.")
                self.exp = int((self.exp % self.exp_for_level))
                self.exp_for_level += int((self.exp_for_level * 0.1))
        return

    def is_dead(self):
        return self.health <= 0

    def attack(self, damage_modifier=1, crit_modifier=0):
        crit_roll = randrange(0, 11)
        if crit_roll > self.crit_chance - crit_modifier:
            return int(randrange(self.damage[0], self.damage[1])*damage_modifier) + self.crit_damage, True
        else:
            return int(randrange(self.damage[0], self.damage[1])*damage_modifier), False

    def regen(self):
        self.health = self.health + self.hp_regeneration if self.health + \
            self.hp_regeneration <= self.max_health else self.max_health
        self.mana = self.mana + self.mp_regeneration if self.mana + \
            self.mp_regeneration <= self.max_mana else self.max_mana



class Npc(ABC):
    def __init__(self, level=1):
        self.level = level
        self.afflictions = []
        self.buffs = []

    def is_dead(self):
        return self.health <= 0

    def attack(self):
        crit_roll = randrange(0, 11)
        if crit_roll > self.crit_chance:
            return self.damage + randrange(1, 4) + self.crit_damage, True
        else:
            return self.damage + randrange(1, 4), False

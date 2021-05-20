from random import randrange


class Character:  # add exp and levels. Health and damage will increase per level
    def __init__(self):
        self.name = ""
        self.currency = 0
        self.exp = 0
        self.exp_for_level = 100
        self.level = 1

    def load_char(self, name, player_stats):
        for key in player_stats.keys():
            if key == name:
                self.name = key
                self.level = player_stats[name]["level"]
                self.exp_for_level = player_stats[name]["exp_for_level"]
                self.exp = player_stats[name]["exp"]
                self.currency = player_stats[name]["coins"]

    def level_up(self):
        if self.exp >= self.exp_for_level:
            for _ in range(self.exp // self.exp_for_level):
                self.level += 1
                print(f"You leveled up! LvL {self.level}")
                self.exp = int((self.exp % self.exp_for_level))
                self.exp_for_level += int((self.exp_for_level * 0.1))
        return

    def is_dead(self):
        return self.health <= 0

    def attack(self):
        crit_roll = randrange(0, 11)
        if crit_roll > self.crit_chance:
            return self.damage + randrange(1, 4) + self.crit_damage, True
        else:
            return self.damage + randrange(1, 4), False

    def regen(self):
        self.health = self.health + self.regeneration if self.health + \
            self.regeneration <= self.maxhealth else self.maxhealth


class Npc:
    def __init__(self, level=1):
        self.level = level

    def is_dead(self):
        return self.health <= 0

    def attack(self):
        crit_roll = randrange(0, 11)
        if crit_roll > self.crit_chance:
            return self.damage + randrange(1, 4) + self.crit_damage, True
        else:
            return self.damage + randrange(1, 4), False

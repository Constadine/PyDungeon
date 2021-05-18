from random import randrange


class Character:  # add exp and levels. Health and damage will increase per level
    def __init__(self):
        pass

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
    def __init__(self):
        pass

    def is_dead(self):
        return self.health <= 0

    def attack(self):
        crit_roll = randrange(0, 11)
        if crit_roll > self.crit_chance:
            return self.damage + randrange(1, 4) + self.crit_damage, True
        else:
            return self.damage + randrange(1, 4), False

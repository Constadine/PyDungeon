from buffs_afflictions import afflictions
from time import sleep
from useful_functions import get_int

def check_afflictions(char,afflictions_dict, duration):

    if "Poison" in char.afflictions:
        if duration is None:
            duration = afflictions_dict["Poison"]["duration"]
        damage = afflictions_dict["Poison"]["damage"]
        char.health -= damage
        duration -= 1

        print(f"{char.name} took {damage} poison damage. ({duration} rounds left)")
        if duration == 0:
            char.afflictions.remove("Poison")
        return duration

class Battle:
    def __init__(self, character, enemy):
        self.character = character
        self.enemy = enemy
        self.kills = 0
        self.exp_gained = 0

    def print_state(self):
        print(f"LvL {self.character.level} {self.character.name} - HP:{self.character.health}/{self.character.max_health} MP:{self.character.mana}/{self.character.max_mana} Exp: {self.character.exp}/{self.character.exp_for_level} Gold: {self.character.currency}")
        print(f"{self.enemy.name} - HP:{self.enemy.health}")

    def fight(self):
        def player_turn(character, enemy):

            while True:
                action_choice = get_int("1-Basic Attack | 2-Skills: ")
                print("-"*15)
                if action_choice == 1:
                    sleep(1)
                    player_damage, crit_check = character.attack()
                    enemy.health -= player_damage
                    if crit_check:
                        print(
                            f"{character.name} landed a critical hit for {player_damage}!")
                    else:
                        print(
                            f"{character.name} dealt {player_damage} to {enemy.name}")
                    sleep(1)
                    break
                elif action_choice == 2:
                    for idx, skill in enumerate(character.skills):
                        print(
                            str(idx+1) + "-" + str(skill.__name__).capitalize().strip("()").replace("_", " "), end=" ")
                    else:
                        skill_choice = get_int("\nChoose a skill: ")

                        player_damage = character.skills[skill_choice - 1](enemy)
                        if isinstance(player_damage, int):
                            if player_damage:
                                enemy.health -= player_damage
                                break
                            else:
                                continue
                        sleep(1)
            if enemy.is_dead():
                print(f"{enemy.name} is dead!")
                self.kills += 1
                exp_gained = self.enemy.max_health//2
                character.exp += exp_gained
                character.level_up()
                sleep(1)
                print(
                    f"You've gained {exp_gained} exp for slaying {enemy.name}.")
                character.regen()
                return True

        def enemy_turn(character, enemy):
            enemy_damage, crit_check = enemy.attack()
            character.health -= enemy_damage
            if crit_check:
                print(
                    f"{enemy.name} landed a critical hit for {enemy_damage}!")
            else:
                print(
                    f"{enemy.name} dealt {enemy_damage} to {character.name}")

            if self.character.is_dead():
                sleep(1)
                print(f"You died.")
                loss_on_death = int(self.character.currency * 0.15)
                self.character.currency -= loss_on_death
                sleep(1)
                print(f"You have paid {loss_on_death} coins for your revival.")
                return True

        while True:
            
            sleep(1)
            print("-"*15)
            self.print_state()
            print("-"*15)

            if self.character.speed > self.enemy.speed:
                sleep(1)

                if player_turn(self.character, self.enemy):  # breaks when someone dies
                    break
                else:

                    enemy_turn(self.character, self.enemy)

            else:
                sleep(1)
                if enemy_turn(self.character, self.enemy):
                    break
                sleep(1)
                if player_turn(self.character, self.enemy):
                    break


            # if self.enemy.is_dead():
            #     self.kills += 1
            #     self.exp_gained = self.enemy.max_health//2
            #     self.character.exp += self.exp_gained
            #     self.character.level_up()
            #     sleep(1)
            #     print(f"{self.enemy.name} is dead!")
            #     print(
            #         f"You've gained {self.exp_gained} exp for slaying {self.enemy.name}.")
            #     self.character.regen()
            #     break

        return self.kills

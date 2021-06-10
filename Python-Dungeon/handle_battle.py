from time import sleep
from useful_functions import get_int


class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy
        self.kills = 0
        self.exp_gained = 0

    def print_state(self):
        print(f"LvL {self.player.level} {self.player.name} - HP:{self.player.health}/{self.player.max_health} MP:{self.player.mana}/{self.player.max_mana} Exp: {self.player.exp}/{self.player.exp_for_level} Gold: {self.player.currency}")
        print(f"{self.enemy.name} - HP:{self.enemy.health}")

    def fight(self):
        def player_turn(player, enemy):

            while True:
                action_choice = get_int("1-Basic Attack | 2-Skills: ")
                print("-"*15)
                if action_choice == 1:
                    sleep(1)
                    player_damage, crit_check = player.attack()
                    enemy.health -= player_damage
                    if crit_check:
                        print(
                            f"{player.name} landed a critical hit for {player_damage}!")
                    else:
                        print(
                            f"{player.name} dealt {player_damage} to {enemy.name}")
                    sleep(1)
                    break
                elif action_choice == 2:
                    for idx, skill in enumerate(player.skills):
                        print(
                            str(idx+1) + "-" + str(skill.__name__).capitalize().strip("()").replace("_", " "), end=" ")
                    else:
                        skill_choice = get_int("\nChoose a skill: ")

                        # please fix this
                        player_damage = player.skills[skill_choice - 1](player)
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
                player.exp += exp_gained
                player.level_up()
                sleep(1)
                print(
                    f"You've gained {exp_gained} exp for slaying {enemy.name}.")
                player.regen()
                return True

        def enemy_turn(player, enemy):
            enemy_damage, crit_check = enemy.attack()
            player.health -= enemy_damage
            if crit_check:
                print(
                    f"{enemy.name} landed a critical hit for {enemy_damage}!")
            else:
                print(
                    f"{enemy.name} dealt {enemy_damage} to {player.name}")

            if self.player.is_dead():
                sleep(1)
                print(f"You died.")
                loss_on_death = int(self.player.currency * 0.15)
                self.player.currency -= loss_on_death
                sleep(1)
                print(f"You have paid {loss_on_death} coins for your revival.")
                return True

        while True:
            sleep(1)
            print("-"*15)
            self.print_state()
            print("-"*15)

            if self.player.speed > self.enemy.speed:
                sleep(1)

                if player_turn(self.player, self.enemy):  # breaks when someone dies
                    break
                else:

                    enemy_turn(self.player, self.enemy)

            else:
                sleep(1)
                if enemy_turn(self.player, self.enemy):
                    break
                sleep(1)
                if player_turn(self.player, self.enemy):
                    break

            # if self.enemy.is_dead():
            #     self.kills += 1
            #     self.exp_gained = self.enemy.max_health//2
            #     self.player.exp += self.exp_gained
            #     self.player.level_up()
            #     sleep(1)
            #     print(f"{self.enemy.name} is dead!")
            #     print(
            #         f"You've gained {self.exp_gained} exp for slaying {self.enemy.name}.")
            #     self.player.regen()
            #     break

        return self.kills

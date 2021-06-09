from time import sleep


class Battle:
    def __init__(self, player, enemy):
        self.player = player
        self.enemy = enemy

    def print_state(self):
        print(f"LvL {self.player.level} {self.player.name} - HP:{self.player.health}/{self.player.max_health} MP:{self.player.mana}/{self.player.max_mana} Exp: {self.player.exp}/{self.player.exp_for_level} Gold: {self.player.currency}")
        print(f"{self.enemy.name} - HP:{self.enemy.health}")

    def fight(self):
        kills = 0
        exp_gained = 0
        while True:
            sleep(1)
            print("-"*15)
            self.print_state()
            print("-"*15)
            input("Press enter to Attack ")
            print("-"*15)

            if self.player.speed > self.enemy.speed:
                sleep(1)

                player_damage, crit_check = self.player.attack()
                self.enemy.health -= player_damage
                if crit_check:
                    print(
                        f"{self.player.name} landed a critical hit for {player_damage}!")
                else:
                    print(
                        f"{self.player.name} dealt {player_damage} to {self.enemy.name}")
                sleep(1)
                if self.enemy.is_dead():
                    print(f"{self.enemy.name} is dead!")
                    kills += 1
                    exp_gained = self.enemy.max_health//2
                    self.player.exp += exp_gained
                    self.player.level_up()
                    sleep(1)
                    print(
                        f"You've gained {exp_gained} exp for slaying {self.enemy.name}.")
                    self.player.regen()
                    break
                enemy_damage, crit_check = self.enemy.attack()
                self.player.health -= enemy_damage
                if crit_check:
                    print(
                        f"{self.enemy.name} landed a critical hit for {enemy_damage}!")
                else:
                    print(
                        f"{self.enemy.name} dealt {enemy_damage} to {self.player.name}")

            else:
                sleep(1)
                enemy_damage, crit_check = self.enemy.attack()
                self.player.health -= enemy_damage
                if crit_check:
                    print(
                        f"{self.enemy.name} landed a critical hit for {enemy_damage}!")
                else:
                    print(
                        f"{self.enemy.name} dealt {enemy_damage} to {self.player.name}")
                sleep(1)
                player_damage, crit_check = self.player.attack()
                self.enemy.health -= player_damage
                if crit_check:
                    print(
                        f"{self.player.name} landed a critical hit for {player_damage}!")
                else:
                    print(
                        f"{self.player.name} dealt {player_damage} to {self.enemy.name}")

            if self.enemy.is_dead():
                kills += 1
                exp_gained = self.enemy.max_health//2
                self.player.exp += exp_gained
                self.player.level_up()
                sleep(1)
                print(f"{self.enemy.name} is dead!")
                print(
                    f"You've gained {exp_gained} exp for slaying {self.enemy.name}.")
                self.player.regen()
                break
            elif self.player.is_dead():
                sleep(1)
                print(f"You died.")
                break

        return kills

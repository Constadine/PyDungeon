import random
import json


try:
    with open("pokemons.json") as f:
        my_pokemon = json.load(f)
except FileNotFoundError:
    my_pokemon = []


evolutions = [['Charmander', 'Charmeleon', 'Charizard'], [
    'Squirtle', 'Warturtle', 'Blastoise'], ['Bulbasaur', 'Ivysaur', 'Venusaur']]


class Pokemon:
    def __init__(self, name, type, level, exp, exp_for_level) -> None:
        self.name = name
        self.type = type
        self.level = level
        self.exp = exp
        self.exp_for_level = exp_for_level

    def earn_exp(self):
        exp_earned = random.randrange(500, 1000)
        print(f"{self.name} won a battle and earned {exp_earned} exp!")
        self.exp += exp_earned
        if self.exp >= self.exp_for_level:
            for x in range(self.exp // self.exp_for_level):
                self.level += 1
                self.exp = int((self.exp % self.exp_for_level))
                self.exp_for_level += int((self.exp_for_level * 0.1))

    def print_stats(self):
        print(f"""
        Name: {self.name}
        Type: {self.type}
        Level: {self.level}
        Exp: {self.exp}
        Exp for level: {self.exp_for_level} ({self.exp_for_level - self.exp} more to reach lvl{self.level + 1})
        """)

    def check_evolution(self):

        # if self.level == 16 or self.level == 36:
        #     print(f"{self.name} is evolving!")
        #     temp_old_name = self.name
        #     for evolution in evolutions:
        #         for idx, name in enumerate(evolution):
        #             if self.name == name and idx != len(evolution) - 1:
        #                 self.name = evolution[idx + 1]
        #                 break
        if self.level == 16:

            temp_old_name = self.name
            for evolution in evolutions:
                for idx, name in enumerate(evolution):
                    if self.name == name and idx != 1:
                        self.name = evolution[idx + 1]
                        print(f"{self.name} is evolving!")
                        print(
                            f"Congratulations! Your {temp_old_name} has evolved into {self.name}!")
                        break

        elif self.level == 36:
            temp_old_name = self.name
            for evolution in evolutions:
                for idx, name in enumerate(evolution):
                    if self.name == name and idx != len(evolution) - 1:
                        self.name = evolution[idx + 1]
                        print(f"{self.name} is evolving!")
                        print(
                            f"Congratulations! Your {temp_old_name} has evolved into {self.name}!")
                        break


for_save = {}
if not my_pokemon:
    temp_name = input("Name :")
    temp_type = input("Type :")
    my_pokemon = Pokemon(temp_name, temp_type, 1, 0, 200)
else:
    my_pokemon = Pokemon(my_pokemon["name"], my_pokemon["type"],
                         my_pokemon["level"], my_pokemon["exp"], my_pokemon["exp_for_level"])

while int(input("1-battle, 2-exit: ")) == 1:

    my_pokemon.print_stats()
    my_pokemon.earn_exp()
    my_pokemon.check_evolution()
    for_save["name"] = my_pokemon.name
    for_save["type"] = my_pokemon.type
    for_save["level"] = my_pokemon.level
    for_save["exp"] = my_pokemon.exp
    for_save["exp_for_level"] = my_pokemon.exp_for_level

else:
    with open("pokemons.json", "w") as f:
        json.dump(for_save, f)

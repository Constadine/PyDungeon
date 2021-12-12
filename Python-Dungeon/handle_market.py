# from items import PotionHolder
from useful_functions import get_int
from list_items import items
from time import sleep

# class Character:
#     money = 500
#     inventory = ["Vigor Root"]

#     def showoff(self):
#         print(f"Money: {self.money}\nItems: {[i for i in self.inventory]}")

class Market:
    def __init__(self, character=None) -> None:
        self.name = character
        self.items = items

    def filter_owned_items(self,character):
        for i, item in reversed(list(enumerate(items))):
            if (item["name"] in character.inventory) and (item["type"] == "permanent" or item["type"] == "one_use") :
                self.items.pop(i)

    def display_items(self):
        if items:
            print("Wares for sale:")
            for i ,item in enumerate(items):
                print(f"{i+1}. {item['name']}")
        else:
            print("Nothing for sale.")
            sleep(1)
    
    def get_description(self):
        if items:
            print("Which item would you like to purchase: ")
            self.display_items()
            choice = get_int("") - 1
            if choice >= len(items):
                print("Invalid choice.")
            else:
                print(items[choice]["description"]+'\n')
        else:
            print("Nothing for sale.")
            sleep(1)


    def buy(self,character):
        if items:
            print("Which item would you like to purchase: ")
            self.display_items()
            choice = get_int("") - 1
            if choice >= len(items):
                print("Invalid choice.")
            else:
                item = self.items[choice]
                cost = item["cost"]
                if character.currency >= cost:
                    character.currency -= cost
                    character.inventory.append(self.items[choice]["name"])
                    
                    print(f"You 've just bought {item['name']} for {cost} gold!")
                    sleep(1)
                else:
                    print(f"Not enough gold. You need {cost - character.currency} more gold.")
                    sleep(1)
        else:
            print("Nothing for sale.")
            sleep(1)


    def use_market(self,character):
        while True:
            self.filter_owned_items(character)
            print(f"LvL {character.level} {character.name} - Gold: {character.currency} ")
            self.display_items()
            choice = get_int("""
            1 - Buy item
            2 - Get Description
            3 - Exit market 
            """)
            print("")

            if choice == 1:
                self.buy(character) 
            elif choice == 2:
                self.get_description()
                sleep(2)
            elif choice == 3:
                break
      
            else:
                print("Wrong input.")




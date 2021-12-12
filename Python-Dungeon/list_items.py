items = [

{
"name": "Potion Holder",
"cost": 150,
"description": "When owned, +1 potion on each run.",
"type": "permanent",
},
            
{
"name": "Vigor Root",
"cost": 200,
"description": "When owned, gain +20 to max health",
"type": "permanent"
},
{
"name": "Lucky Penny",
"cost": 100,
"description": "When hold, double the money found on explorations. Expires after each run.",
"type": "one_use"
}
]
# inventory = ["Vigor Root", "Lucky Penny"]

# for i, owned_item in reversed(list(enumerate(inventory))):
#         print(inventory)
#         for item in items:

#             if (owned_item == item['name']) and (item['type'] == 'one_use'):
#                 print(f"{owned_item} is {item['type']} so it popped")
#                 inventory.pop(i)
# print(inventory)
#File Objects

from Faction_V1 import *
from Season import *
from Provinces import *

#Faction Initialization

faction1 = Faction('Gaul', 0, 0, 0, 50, None, None)

faction1.add_province(province1)
faction1.population = faction1.faction_sum()
# print(faction1.population)
# print(f"The owner of {province1['name']} is {province1['owner']}")

faction1.add_province(province2)
#province2.change_owner(None, faction1)
faction1.population = faction1.faction_sum()
# print(faction1.population)
# print(f"The owner of {province2['name']} is {province2['owner']}")

#faction1.print_provinces()

Player = Faction

#Beginning of Game Loop Code

game_running = True
session_running = True
global turn
turn = 1

while game_running:
    season = Season('Spring', 1)
    print(f"{season.name}, turn {turn}" )

    while session_running:


        print(f"{season.name}, turn {turn}" )
        print(f"{faction1.treasury} denarii")
        print("Make Your Turn Decision")
        print("[1] Print Faction Information")
        print("[2] Print Province Information")
        print("[3] Upgrade Province")
        print("[4] End/Pass Turn")
        turn_choice = input()
        if turn_choice == '1':
            print(faction1.treasury, faction1.population, faction1.size)
        elif turn_choice == '2':
            print(faction1.provinces)
        elif turn_choice == '3':
            turn += 1
            faction1.manage_province(province1, turn, season)
            season.change_season()
            faction1.earn_province_income(faction1.provinces)
        elif turn_choice == '4':
            turn += 1
            season.change_season()
            faction1.earn_province_income(faction1.provinces)
        else:
            print("Sorry, please try again")

#Main_V2

#File Imports

from Faction import *
from Season import *
from Provinces import *


#Pre-Game Loop Initialization Code
#Initializing Boolean and Counter Values

game_running = True
campaign_loop = True
session_running = True
global turn
turn = 1

#Core Game Loop

while game_running:
    #Faction Initialization
    faction1 = Faction('Gaul', 0, 0, 0, 50, None, None)
    faction2 = Faction('Rome', 0, 0, 0, 50, None, None)
    faction3 = Faction('Greece', 0, 0, 0, 50, None, None)
    faction4 = Faction('Germania', 0, 0, 0, 50, None, None)
    faction_array = [faction1, faction2, faction3, faction4]
    Player = Faction

    #Setting baseline season value
    season = Season('Spring', 1)

    #Game Bootup Menu
    print("Welcome to Europa Barbarorum")
    print("Make a choice:")
    print("[1] Launch New Campaign")
    print("[2] Custom Battle")
    print("[3] Exit Program")
    game_choice = input()
    if game_choice == '1':
        print("Game Starting")
        session_running = True
        campaign_loop = True
    elif game_choice == '2':
        print("Feature currently not enabled (2/23/2020 version")
        #Insert activation code rooted in Fight.py
    elif game_choice == '3':
        print("Closing Program")
        session_running = False
        game_running = False
        campaign_loop = False
    else:
        print("Please try again")

    #Campaign Selection Menu 
    while campaign_loop == True:
        
        print("Choose your faction")
        faction_number = 0 
        for faction in faction_array:
            faction_number += 1
            print(f"[{faction_number}] {faction.name}")
        print(f"[x] Exit the faction selection menu")
        faction_choice = input()
        if faction_choice <= 'faction_number':
            selected_faction = faction_array[int(faction_choice) - 1]
            session_running = True
            Player = selected_faction
            print(f"You are {Player.name}")
            print(f"Provinces: {Player.size}, Population: {Player.population}, Income: {Player.income}, "
                    f"Treasury: {Player.treasury}, Manpower: {Player.manpower}")
        elif faction_choice == 'x':
            print("Exiting this menu")
            campaign_loop = False
            session_running = False
        else:
            print("Error, please try again")
            session_running = False

        while session_running:
            
            turn_options = ["[1] Print Faction Information", "[2] Print Province Information", "[3] Upgrade Province", "[4] Claim Unowned Province",
              "[5] Build Army", "[6] End Turn", "[7] End Session"  ]

            print(f"{season.name}, turn {turn}" )
            print(f"You have {Player.treasury} denarii and {Player.population} population")
            print("Make Your Turn Decision")
            counter = 0
            for option in turn_options:
                print(turn_options[counter])
                counter += 1
            turn_choice = input()
            if turn_choice == '1':
                print(f" You have {Player.treasury} gold, {Player.population} population, and {Player.size} provinces")
                print(f" Your income is {Player.income} gold per turn")
            elif turn_choice == '2':
                Player.print_provinces()
            elif turn_choice == '3':
                Player.manage_province(turn, season, Player)
            elif turn_choice == '4':
                Player.claim_province(Player, Player.provinces)
            elif turn_choice == '5':
                print("Note: Unsupported Feature (2020/2/23 Version)")
                #Player.add_army

            elif turn_choice == '6':
                turn += 1
                season.change_season()
                Player.earn_province_income(Player.provinces)
            elif turn_choice == '7':
                print("Exiting Session")
                session_running = False
            else:
                print("Sorry, please try again")

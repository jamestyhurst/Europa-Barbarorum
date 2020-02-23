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
    print("[1] Start Game")
    print("[2] Exit Program")
    game_choice = input()
    if game_choice == '1':
        print("Game Starting")
        session_running = True
        campaign_loop = True
    elif game_choice == '2':
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


            print(f"{season.name}, turn {turn}" )
            print(f"You have {Player.treasury} denarii and {Player.population} population")
            print("Make Your Turn Decision")
            print("[1] Print Faction Information")
            print("[2] Print Province Information")
            print("[3] Upgrade Province")
            print("[4] Claim Unowned Province")
            print("[5] End Turn")
            print("[6] End Session")
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
                turn += 1
                season.change_season()
                Player.earn_province_income(Player.provinces)
            elif turn_choice == '6':
                print("Exiting Session")
                session_running = False
            else:
                print("Sorry, please try again")

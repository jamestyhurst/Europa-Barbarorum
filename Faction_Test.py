#Faction V2

from Provinces import *
from Season import *

class Faction:

    number_of_factions = 0
    improvement_amount = 1.05
    growth_amount = 1.05
    manpower_modifier = 0.25
    faction_list = []

    def __init__(self, name, size, income, population, treasury, provinces=None, armies = None):
        self.name = name
        self.size = size
        self.income = income
        self.population = population
        self.manpower = population * self.manpower_modifier
        self.treasury = treasury

        #print(f"The Faction of {self.name} is in this game")

        if provinces is None:
            self.provinces = []
        else:
            self.provinces = provinces
            self.update_population()
        if armies is None:
            self.armies = []
        else:
            self.armies = armies

        Faction.number_of_factions += 1
        if Faction not in self.faction_list:
            self.faction_list.append(Faction)

    
    def update_population(self):
        faction_population = 0
        for province in self.provinces:
            faction_population += province['population']
        self.population = faction_population


    def add_province(self, province):
        if province not in self.provinces:
            self.provinces.append(province)
            self.size = self.size + 1
            province['owner'] = self.name
            self.update_population()

    def remove_province(self, province):
        if province in self.provinces:
            self.provinces.remove(province)
            self.size = self.size - 1
            self.update_population()

    def claim_province(self, Player, provinces):
        choice_loop = True
        action_loop = True
        while choice_loop == True:
            print("Claim an unowned province")
            action_loop == True
            option_number = 0
            option_array = []
            for province in ProvinceArray:
                if province['owner'] is None:
                    option_number += 1
                    option_array.append(province)
                    print(f"[{option_number}] {province['name']} , owner: {province['owner']},"
                            f"income: {province['income']}, population: {province['population']}")
                
                   
              
                    
            print("Choose a province (or press x to return to previous menu)")
            province_selection = input()
            if province_selection <= 'option_number':
                selected_province = option_array[int(province_selection) - 1]
                print(selected_province)
            elif province_selection == 'x':
                print("Exiting Menu")
                action_loop = False
                choice_loop = False
            else:
                print("Please Try Again")
                action_loop = False

            while action_loop == True:
                print(f"Make your decision, you have {Player.treasury} gold")
                print("[1] Seize this province (50 gold)")
                print("[x] Exit this menu")
                province_choice = input()
                if province_choice == '1':
                    if self.treasury >= 50:
                        self.treasury -= 50
                        self.add_province(selected_province)
                        action_loop = False
                        print(f"Province of {selected_province['name']} Seized by {self.name}")
                        print(" ")
                    else: 
                        print("Not enough funds")
                elif province_choice == 'x':
                    print("Exiting this menu")
                    action_loop = False
                else:
                    print("Please Try Again")
            self.update_population()

    #Intended for a Factional Ledger Operation
    def print_provinces(self):
        for province in self.provinces:
            print(f"Provinces of {self.name}, total of {self.size}")
            print(f"--> {province['name']}, {province['population']} people, income of {province['income']}" )

    def faction_sum(self):
        for province in self.provinces:
            self.population += province['population']
            return self.population

    #Province-based income function, intended for when the turn ends
    def earn_province_income(self, provinces):
        for province in provinces:
            self.treasury = self.treasury + province['income']

    #Provincial Economy Upgrade Function
    def improve_province(self, province):
        if province in self.provinces:
            province['income'] = province['income'] * self.improvement_amount

    #Population growth function
    def grow_province(self, province):
        if province in self.provinces:
            province['population'] = province['population'] * self.growth_amount

    #Function for selecting and improving provinces
    def manage_province(self, turn, season, Player):
        #Boolean loop value initializations
        choice_loop = True
        action_loop = True
        #if statement to check if Player actually has provinces to upgrade
        if self.provinces == []:
            print(' ')
            print("[!] First claim a province before attempting to upgrade a province")
            print(' ')
            action_loop = False
            choice_loop = False
        #Selection loop
        while choice_loop == True:
            action_loop == True
            option_number = 0
            option_array = []
            for province in ProvinceArray:
                if province in self.provinces:
                    option_number += 1
                    print(f"[{option_number}] {province['name']} (owned by Player)")
                    option_array.append(province)
            print("Choose a province (or press x to return to previous menu)")
            province_selection = input()
            if province_selection <= 'option_number':
                selected_province = option_array[int(province_selection) - 1]
                print(selected_province)
            elif province_selection == 'x':
                print("Exiting Menu")
                action_loop = False
                choice_loop = False
            else:
                print("Please Try Again")
                action_loop = False


            #Post-selection management loop
            while action_loop == True:
                print(f"Select a Province-Management-Option, you have {Player.treasury} gold")
                print("[1] Improve Income (50 Gold)")
                print("[2] Grow Population (50 Gold)")
                print("[3] Return to Province Selection Menu")
                province_choice = input()
                if province_choice == '1':
                    if self.treasury >= 50:
                        self.treasury -= 50
                        self.improve_province(selected_province)
                        action_loop = False
                        print("Provincial Economy Updgraded")
                        print(" ")
                    else: 
                        print("Not enough funds")
                elif province_choice == '2':
                    if self.treasury >= 50:
                        self.treasury -= 50
                        self.grow_province(selected_province)
                        action_loop = False
                        print("Provincial Population Expanded")
                        print(" ")
                    else: 
                        print("Not enough funds")
                elif province_choice == '3':
                    print("Returning to Province Selection Menu")
                    action_loop = False

                else:
                    print("Please Try Again")

    def add_army(self, army):
        if army not in self.armies:
            self.armies.append(army)

    def remove_army(self, army):
        if army in self.armies:
            self.armies.remove(army)


    def print_armies(self):
        for army in self.armies:
            print(f"Armies of {self.name}, total of {self.armies}")
            print(f'--> Army #{army.number}, {army.size} men' )



    #Below is legacy code from previous versions or which is not conveinent to have active in the current version


    # def Faction_Facts(self):
    #     return '{}, {} province(s), {} income, {} population, {} gold'.format(self.name,
    #                                                                           self.size,
    #                                                                           self.income,
    #                                                                           self.population, self.treasury)
    #
   
# class non_player(Faction):
#     number_of_npcs = 0
#     npc_list = []
#     def __init__(self, name):
#         super().__init__(name)
#         #self.treasury = treasury
#
#         non_player.number_of_npcs += 1
#         if non_player not in self.npc_list:
#             self.npc_list.append(non_player)

    # def __init__(self, name, size, income, population, treasury, provinces = None):
    #     super().__init__(name, size, income, population, treasury, provinces = None)
    #     self.treasury = treasury
    #
    #     non_player.number_of_npcs += 1
    #     if non_player not in self.npc_list:
    #         self.npc_list.append(non_player)
    #
    # @classmethod
    # def all_npcs_improve_economy(cls):
    #     print("All NPC's have chosen to improve their economies this turn")
    #     for npc in cls.npc_list:
    #         super().improve_economy(npc)
    #

    # @classmethod
    # def npc_income(cls):
    #     for npc in non_player:
    #         cls.treasury = cls.treasury + cls.income



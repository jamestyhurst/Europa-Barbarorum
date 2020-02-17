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

        print(f"The Faction of {self.name}")

        if provinces is None:
            self.provinces = []
        else:
            self.provinces = provinces
            self.population = provinces.size
        if armies is None:
            self.armies = []
        else:
            self.armies = armies

        Faction.number_of_factions += 1
        if Faction not in self.faction_list:
            self.faction_list.append(Faction)

    def add_province(self, province):
        if province not in self.provinces:
            self.provinces.append(province)
            self.size = self.size + 1
            province['owner'] = self.name

    def remove_province(self, province):
        if province in self.provinces:
            self.provinces.remove(province)
            self.size = self.size - 1

    def print_provinces(self):
        for province in self.provinces:
            print(f"Provinces of {self.name}, total of {self.size}")
            print(f"--> {province['name']}, {province['population']} people" )

    def faction_sum(self):
        for province in self.provinces:
            self.population += province['population']
            return self.population


    def earn_province_income(self, provinces):
        for province in provinces:
            self.treasury = self.treasury + province['income']

    def improve_province(self, province):
        if province in self.provinces:
            province['income'] = province['income'] * self.improvement_amount

    def grow_province(self, province):
        if province in self.provinces:
            province['population'] = province['population'] * self.growth_amount

    def manage_province(self, province, turn, season):
        choice_loop = True
        action_loop = True
        while choice_loop == True:
            action_loop == True
            option_number = 0
            province_numbers = []
            for province in ProinceArray:
                if province in self.provinces:
                    option_number += 1
                    print(f"{[option_number]} {province['name']} (owned by faction)"
                    province_numbers.append(option_number)
                elif province not in self.provinces: 
                    option_number += 1
                     print(f"{[option_number]} {province['name']} (NOT owned by faction)")"
                     province_numbers.append(option_number)
            print("Choose a province (or press x to return to previous menu)")
            province_selection = input()
            if province_selection == '1' and ProvinceArray[0] in self.provinces:
                selected_province = ProvinceArray[0]
                print(f"The Province of {ProvinceArray[0]['name']}")
            elif province_selection == '2' and ProvinceArray[1] in self.provinces::
                selected_province = ProvinceArray[1]
                print(f"The Province of {ProvinceArray[1]['name']}")
            elif province_selection == '3' and ProvinceArray[2] in self.provinces::
                selected_province = ProvinceArray[2]
                print(f"The Province of {ProvinceArray[2]['name']}")
            elif province_selection == '4' and ProvinceArray[3] in self.provinces::
                selected_province = ProvinceArray[3]
                print(f"The Province of {ProvinceArray[3]['name']}")
            elif province_selection = 'x':
                print("Exiting Menu")
                action_loop = False
                choice_loop = False
            else:
                print("Please Try Again")



            while action_loop == True:
                print("Select a Province-Management-Option")
                print("[1] Improve Income (50 Gold)")
                print("[2] Grow Population (50 Gold)")
                print("[3] Return to Province Selection Menu")
                province_choice = input()
                if province_choice == '1':
                    if self.treasury >= 50:
                        self.treasury -= 50
                        self.improve_province(selected_province)
                        action_loop = False
                        turn = turn + 1
                        season.change_season()
                    else: 
                        print("Not enough funds")
                elif province_choice == '2':
                    if self.treasury >= 50:
                        self.treasury -= 50
                        self.grow_province(selected_province)
                        action_loop = False
                        turn = turn + 1
                        season.change_season()
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
    # def improve_economy(self):
    #     self.income = int(self.income * self.improvement_amount)
    #     #Can also type "Faction.improvement_amount"
    #
    # @classmethod
    # def all_factions_earn(cls):
    #     for faction in faction_list:
    #         faction.treasury = faction.treasury + faction.income
    #
    # @classmethod
    # def all_factions_grow(cls):
    #     for faction in faction_list:
    #         faction.population = faction.population * faction.growth_amount
    #
    # @classmethod
    # def set_improvement_amount(cls, amount):
    #     cls.improvement_amount = amount
    #
    # @classmethod
    # def fromstring(cls, faction_string):
    #     name, size, income, population = faction_string.split('-')
    #     return cls(name, size, income, population)

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


    # def earn_income(self, treasury, income):
    #     self.treasury = int(treasury + income)
    #
    # def grow_population(self):
    #     self.population = int(self.population * self.growth_amount)
    #
    # def increase_growth_amount(self):
    #     self.growth_amount += 0.05


# faction1 = Faction('Gaul', 0, 0, 0, 0, None, None)
#
# faction1.add_province(province1, faction1)
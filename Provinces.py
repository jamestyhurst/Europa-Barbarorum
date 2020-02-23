#Defining generic baseline income levels of provinces
income_level_1 = 25
income_level_2 = 50
#Defining generic baseline population levels of provinces
population_level_1 = 500
population_level_2 = 1000
#List of Provinces:
#(Current Version, 2/23/2020: Each faction has an upper-income province and a lower-income province)
#"Core Gallic Provinces"
province1 = {'name': 'Lugdunum', 'population': population_level_2, 'income': income_level_2, 'owner': None}
province2 = {'name': 'Bibracte', 'population': population_level_1, 'income': income_level_1, 'owner': None}
#"Core Roman Provinces"
province3 = {'name': 'Rome', 'population': population_level_2, 'income': income_level_2, 'owner': None}
province4 = {'name': 'Capua', 'population': population_level_1, 'income': income_level_1, 'owner': None}
#"Core Greek Provinces"
province5 = {'name': 'Attica', 'population': population_level_2, 'income': income_level_2, 'owner': None}
province6 = {'name': 'Euboea', 'population': population_level_1, 'income': income_level_1, 'owner': None}
#"Core Germanic Provinces"
province7 = {'name': 'Macromania', 'population': population_level_2, 'income': income_level_2, 'owner': None}
province8 = {'name': 'Lugia', 'population': population_level_1, 'income': income_level_1, 'owner': None}

ProvinceArray = [ province1, province2, province3, province4, province5, province6, province7, province8 ]
#PopulationArray = [ province1, province2, province3, province4, province5, province6, province7, province8 ]






# from Faction_V1 import faction1

# class Province:
#     def __init__(self, name, size, owner):
#         self.name = str(name)
#         self.size = int(size)
#         self.owner = owner
#
#     def __add__(self, other):
#         return self.size + other.size
#
#     def change_owner(self, loser, taker):
#         self.loser = loser
#         self.taker = taker
#         if loser is self.owner:
#             self.owner.remove(loser)
#         if taker is not self.owner:
#             self.owner.append(taker)


    # def print_provinces(self, owner):
    #     for province in owner.provinces:
    #         print(f"Provinces of {owner.name}, total of {owner.provinces}")
    #         print(f'--> {province.name}, {province.size} people' )

# province1 = Province('Lugdunum', 1000, faction1)
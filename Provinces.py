#Defining generic baseline income levels of provinces
income_level_1 = 25
income_level_2 = 50
#Defining generic baseline population levels of provinces
population_level_1 = 500
population_level_2 = 1000
#List of Provinces:
#(Current Version, 2/23/2020: Each faction has an upper-income province and a lower-income province)
#"Core Gallic Provinces"
province1 = {'name': 'Northern Gaul', 'population': population_level_2, 'income': income_level_2, 'owner': None}
province2 = {'name': 'Southern Gaul', 'population': population_level_1, 'income': income_level_1, 'owner': None}
#"Core Roman Provinces"
province3 = {'name': 'Central Italy', 'population': population_level_2, 'income': income_level_2, 'owner': None}
province4 = {'name': 'Southern Italy', 'population': population_level_1, 'income': income_level_1, 'owner': None}
#"Core Greek Provinces"
province5 = {'name': 'Attica', 'population': population_level_2, 'income': income_level_2, 'owner': None}
province6 = {'name': 'Laconica', 'population': population_level_1, 'income': income_level_1, 'owner': None}
#"Core Germanic Provinces"
province7 = {'name': 'Northern Germania', 'population': population_level_2, 'income': income_level_2, 'owner': None}
province8 = {'name': 'Western Germania', 'population': population_level_1, 'income': income_level_1, 'owner': None}

province9 = {'name': 'Africa', 'population': population_level_2, 'income': income_level_2, 'owner': None}
province10 = {'name': 'Libya', 'population': population_level_1, 'income': income_level_1, 'owner': None}

province11 = {'name': 'Britannia', 'population': population_level_2, 'income': income_level_2, 'owner': None}
province12 = {'name': 'Hibernia', 'population': population_level_1, 'income': income_level_1, 'owner': None}

province13 = {'name': 'Macedonia', 'population': population_level_2, 'income': income_level_2, 'owner': None}
province14 = {'name': 'Thrace', 'population': population_level_1, 'income': income_level_1, 'owner': None}

ProvinceArray = [ province1, province2, province3, province4, province5, province6, province7, province8, province9, province10, 
province11 , province12, province13, province14   ]
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
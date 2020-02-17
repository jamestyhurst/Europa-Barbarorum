province1 = {'name': 'Lugdunum', 'population': 1000, 'income': 10, 'owner': None}
province2 = {'name': 'Bibracte', 'population': 1000, 'income': 10, 'owner': None}
province3 = {'name': 'Rome', 'population': 1000, 'income': 10, 'owner': None}
province4 = {'name': 'Capua', 'population': 1000, 'income': 10, 'owner': None}

provinceArray = {province1, province2, province3, province4}






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
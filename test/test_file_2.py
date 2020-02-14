# class Test_Class_2:
#     def __init__(self):
#         with open('test_file_1.py', 'w') as f:
#             write("test_object_2 = Test_Class_1[2]")

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

    def add_province(self, province, owner):
        if province not in self.provinces:
            self.provinces.append(province)
            #self.size = self.size + 1
            #province.owner = owner

    def remove_province(self, province):
        if province in self.provinces:
            self.provinces.remove(province)
            self.size = self.size - 1

    def print_provinces(self):
        for province in self.provinces:
            print(f"Provinces of {self.name}, total of {self.provinces}")
            print(f'--> {province.name}, {province.name} people' )

    def faction_sum(self):
        for province in self.provinces:
            self.population += province.size
            return self.population

    def earn_province_income(self, provinces):
        for province in provinces:
            self.treasury = self.treasury + province['income']


faction1 = Faction('Gaul', 0, 0, 0, 0, None, None)


province1 = {'name': 'Lugdunum', 'population': 1000, 'income': 10}
province2 = {'name': 'Bibracte', 'population': 1000, 'income': 10}


faction1.add_province(province1, faction1)
faction1.population = province1['population']
print(faction1.population)
print(f"The owner of {province1['name']} is {faction1.name}")
faction1.earn_province_income(faction1.provinces)
print(faction1.treasury)

faction1.add_province(province2, faction1)
faction1.population = province1['population'] + province2['population']
print(faction1.population)
print(f"The owner of {province2['name']} is {faction1.name}")
faction1.earn_province_income(faction1.provinces)
print(f"The Faction of {faction1.name} has a population of {faction1.population}")
print(faction1.treasury)
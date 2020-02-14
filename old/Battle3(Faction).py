class Faction:

    number_of_factions = 0
    improvement_amount = 1.05

    def __init__(self, name, size, income, population, provinces=None):
        self.name = name
        self.size = size
        self.income = income
        self.population = population
        self.manpower = population * 0.25
        self.treasury = 0

        if provinces is None:
            self.provinces = []
        else:
            self.provinces = provinces

        Faction.number_of_factions += 1

    def earn_income(self, treasury, income):
        self.treasury = treasury + income

    def add_province(self, province):
        if province not in self.provinces:
            self.cities.append(province)

    def remove_province(self, province):
        if province in self.provinces:
            self.provinces.remove(province)

    def print_cities(self):
        for province in self.provinces:
            print(f'--> {province.name}, {province.size} people' )

    def Faction_Facts(self):
        return '{}, {} province'.format(self.name, self.size)

    def improve_economy(self):
        self.income = int(self.income * self.improvement_amount)
        #Can also type "Faction.improvement_amount"

    @classmethod
    def set_improvement_amount(cls, amount):
        cls.improvement_amount = amount

    @classmethod
    def fromstring(cls, faction_string):
        name, size, income, population = faction_string.split('-')
        return cls(name, size, income, population)


class Province:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __add__(self, other):
        return self.size + other.size

class Season:
    def __init__(self, name, quarter):
        self.name = name
        self.quarter = quarter

    def change_season(self):
        if self.quarter == 2:
            self.quarter += 1
            self.name = 'Fall'
        elif self.quarter == 3:
            self.quarter +=1
            self.name = 'Winter'
        elif self.quarter == 1:
            self.quarter +=1
            self.name = 'Summer'
        elif self.quarter == 4:
            self.quarter = self.quarter - 3
            self. name = 'Spring'

season = Season('Spring', 1)
print(season.name, season.quarter)

province1 = ['Latinum', 1000]
province2 = ['Euboea', 1000]
province3 = ['Macromania', 1000]
province4 = ['Bibracte', 1000]

faction1 = Faction('Rome', 1, 100, 1000, [province1])
faction2 = Faction('Greece', 1, 100, 1000, [province2])
faction3 = Faction('Germania', 1, 100, 1000, [province3])
faction4 = Faction('Gaul', 1, 100, 1000, [province4])

Player = Faction

game_running = True
session_running = True

while game_running:
    print("Choose your faction")
    print("[1] for Rome")
    print("[2] for Greece")
    print("[3] for Germania")
    print("[4] for Gaul")
    faction_choice = input()
    if faction_choice == '1':
        Player = faction1
    elif faction_choice == '2':
        Player = faction2
    elif faction_choice == '3':
        Player = faction3
    elif faction_choice == '4':
        Player = faction4
    else:
        print("Error, please try again")
        null_string = ('Null-0-0-4')
        Player = Faction.fromstring(null_string)


    print(f"You are {Player.name}")
    print(f"Provinces: {Player.provinces}, Population: {Player.population}, Income: {Player.income}, "
          f"Treasury: {Player.treasury}, Manpower: {Player.manpower}")

    while session_running:
            print("What will you do this turn?")
            print("[1] Develop Economy")
            print("[2] Exit Game")
            turn_choice = input()
            if turn_choice == '1':
                Faction.improve_economy(Player)
                Faction.earn_income(Player, Player.treasury, Player.income)
                print(Player.income)
                print(Player.treasury)
            elif turn_choice == '2':
                session_running = False
                print("Game ended")
            else:
                print("Error, please try again")





# Civilized_1.population = City.__add__(city3, city4)
# print(Civilized_1.population)

# class Barbarian(Faction):
#
#     improvement_amount = 1.10
#
#     def __init__(self, name, size, income, population, lead_tribe):
#         super().__init__(name, size, income, population)
#         self.lead_tribe = lead_tribe
#
# class Civilized(Faction):
#
#     def __init__(self, name, size, income, population, cities=None):
#         super().__init__(name, size, income, population)
#         if cities is None:
#             self.cities = []
#         else:
#             self.cities = cities
#
#     def add_city(self, city):
#         if city not in self.cities:
#             self.cities.append(city)
#
#     def remove_cities(self, city):
#         if city in self.cities:
#             self.cities.remove(city)
#
#     def print_cities(self):
#         for city in self.cities:
#             print(f'--> {city.name}, {city.size} people' )
#
# class City:
#     def __init__(self, name, size):
#         self.name = name
#         self.size = size
#
#     def __add__(self, other):
#         return self.size + other.size

# city1 = City('Athens', 5000)
# city2 = City('Sparta', 5000)
# city3 = City('Rome', 5000)
# city4 = City('Capua', 5000)

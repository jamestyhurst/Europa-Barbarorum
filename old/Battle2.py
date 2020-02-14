class Faction:

    number_of_factions = 0
    improvement_amount = 1.05

    def __init__(self, name, size, income, population):
        self.name = name
        self.size = size
        self.income = income
        self.population = population
        self.manpower = population * 0.25

        Faction.number_of_factions += 1

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


class Barbarian(Faction):

    improvement_amount = 1.10

    def __init__(self, name, size, income, population, lead_tribe):
        super().__init__(name, size, income, population)
        self.lead_tribe = lead_tribe

class Civilized(Faction):

    def __init__(self, name, size, income, population, cities=None):
        super().__init__(name, size, income, population)
        if cities is None:
            self.cities = []
        else:
            self.cities = cities

    def add_city(self, city):
        if city not in self.cities:
            self.cities.append(city)

    def remove_cities(self, city):
        if city in self.cities:
            self.cities.remove(city)

    def print_cities(self):
        for city in self.cities:
            print(f'--> {city.name}, {city.size} people' )

class City:
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

Season.change_season(season)
print(season.name, season.quarter)

Season.change_season(season)
print(season.name, season.quarter)

Season.change_season(season)
print(season.name, season.quarter)

Season.change_season(season)
print(season.name, season.quarter)

city1 = City('Athens', 5000)
city2 = City('Sparta', 5000)
city3 = City('Rome', 5000)
city4 = City('Capua', 5000)

Civilized_1 = Civilized('Rome', 1, 100, 1000, [city3])
Civilized_2 = Civilized('Greece', 1, 100, 1000, [city1])

Civilized_1.add_city(city4)
Civilized_2.add_city(city2)

Civilized_1.print_cities()
Civilized_2.print_cities()

Civilized_1.population = City.__add__(city3, city4)
print(Civilized_1.population)


Barbarian_1 = Barbarian('Germania', 1, 100, 1000, 'Suebi')
Barbarian_2 = Barbarian('Gaul', 1, 100, 1000, 'Aedui')

#faction_string1 = 'Rome-1-100-1000'
#faction_string2 = 'Gaul-1-100-1000'


#new_faction1 = Faction.fromstring(faction_string1)

#print(new_faction1.__dict__)

#print(Faction.number_of_factions)

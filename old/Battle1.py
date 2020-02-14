#First as practice space, secondly as strategic-level code

#defining faction class;
# size = number of provinces


class Faction:

    number_of_factions = 0
    improvement_amount = 1.05

    def __init__(self, name, size, income, population):
        self.name = name
        self.size = size
        self.income = income
        self.population = population
        #self.manpower = population * 0.25

        Faction.number_of_factions += 1

    def Faction_Facts(self):
        return '{}, {} province'.format(self.name, self.size)

    def improve_economy(self):
        self.income = int(self.income * self.improvement_amount)
        #Can also type "self.improvement_amount"

    @classmethod
    def set_improvement_amount(cls, amount):
        cls.improvement_amount = amount

    @classmethod
    def fromstring(cls, faction_string):
        name, size, income, population = faction_string.split('-')
        return cls(name, size, income, population)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False

        return True

    def __repr__(self):
        return "Faction('{}', '{}', '{}', '{}')".format(self.name, self.size, self.income, self.population)

    def __str__(self):
        return '{} - {}'.format(self.Faction_Facts(), self.population)



class Barbarian(Faction):

    improvement_amount = 1.10

    def __init__(self, name, size, income, population, lead_tribe):
        super().__init__(name, size, income, population)
        self.lead_tribe = lead_tribe

class Civilized(Faction):

    def __init__(self, name, size, income, population, capital=None):
        super().__init__(name, size, income, population)
        if capital is None:
            self.capital = []
        else:
            self.capital = capital

    def add_capital(self, city):
        if city not in self.capital:
            self.capital.append(city)

    def remove_capital(self, city):
        if city in self.capital:
            self.capital.remove(city)

    def print_capitals(self):
        for city in self.capital:
            print('-->', city)

class City:
    def __init__(self, name, size):
        self.name = name
        self.size = size

    def __add__(self, other):
        return self.size + other.size

    def __len__(self):
        return len(self.name)


city1 = City('Athens', 5000)
city2 = City('Sparta', 5000)

print(len(city1))

print(city1 + city2)

faction_1 = Faction('Rome', 1, 100, 1000)
faction_2 = Faction('Gaul', 1, 100, 1000)

Civilized_1=Civilized('Greece', 1, 100, 1000, [city1])
#print(Civilized_1.Faction_Facts())
Civilized_1.add_capital(city2)
Civilized_1.remove_capital(city1)
#print(Civilized_1.capital)
Civilized_1.print_capitals()

Barbarian_1 = Barbarian('Germania', 1, 100, 1000, 'Suebi')

print(Barbarian_1.Faction_Facts())
print(Barbarian_1.lead_tribe)



#print(faction_1)
#print(repr(faction_1))
#print(str(faction_1))

#print(faction_1.__repr__())
#print(faction_1.__str__())

#print(isinstance(Barbarian_1, Barbarian))
#print(isinstance(Barbarian_1, Civilized))
#print(issubclass(Barbarian, Civilized))

#print(Barbarian_1.income)
#Barbarian_1.improve_economy()
#print(Barbarian_1.income)

#faction_string1 = 'Rome-1-100-1000'
#faction_string2 = 'Gaul-1-100-1000'


#new_faction1 = Faction.fromstring(faction_string1)

#print(new_faction1.__dict__)

#print(Faction.number_of_factions)
#print(faction_1.Faction_Facts())
#faction_1.improvement_amount = 1.10

#print(faction_1.__dict__)
#print(faction_2.__dict__)

#print(Faction.improvement_amount)
#print(faction_1.improvement_amount)
#print(faction_2.improvement_amount)

#import _datetime

#my_date = _datetime.date(2020, 2, 1)
#print(Faction.is_workday(my_date))
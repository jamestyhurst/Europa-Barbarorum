import random

EconomicOutput = [random.randint(1, 1000), random.randint(1, 1000)]
ProductionModifier = [random.randint(1, 10), random.randint(1, 10)]
ProductionOutput = [EconomicOutput[0]*ProductionModifier[0], EconomicOutput[1]*ProductionModifier[1]]

Faction1 = {'name': 'Rome', 'Economy': EconomicOutput[0], 'Production Modifier': ProductionModifier[0],
            'Production Output': ProductionOutput[0]}
Faction2 = {'name': 'Gaul', 'Economy': EconomicOutput[1], 'Production Modifier': ProductionModifier[1],
            'Production Output': ProductionOutput[1]}

#print(Faction1)
#print(Faction2)

print(f"The Roman economic output this year was equal to {Faction1['Economy']} Sesterses")
print(f"The Roman production modifier this year was equal to {Faction1['Production Modifier']} out of 10")
print(f"Total Roman production this year was equal to {Faction1['Production Output']}")
print("")
print(f"The Gallic economic output this year was equal to {Faction2['Economy']} Sesterses")
print(f"The Gallic production modifier this year was equal to {Faction2['Production Modifier']} out of 10")
print(f"Total Gallic production this year was equal to {Faction2['Production Output']}")
print("                                                                                  ")

print("The armies of Rome and Gaul met in the field this year")
Attacker = random.randint(1, 2)
if Attacker ==1:
    print("Rome was the attacker")
else:
    print("Gaul was the attacker")
print("A battle occurred between the two armies; The fighting was bitter, the losing side resisting to the last man.")
print("______________________")

ArmySize = [Faction1['Production Output'], Faction2['Production Output']]

# "Dice roll" function
positioning = [random.randint(1, 6), random.randint(1, 6)]

CombatPerformance = [(random.randint(1, 6)*positioning[0]), (random.randint(1, 6)*positioning[1])]

CombatOutput = [(ArmySize[0]*CombatPerformance[0]), (ArmySize[1]*CombatPerformance[1])]

casualties = [0, 0]

RomeArmy = {'Army Size': ArmySize[0], "Positioning Value": positioning[0], 'Combat Quality': CombatPerformance[0],
                'Total Combat Value': CombatOutput[0], 'Name': 'The Roman Army', 'Casualties': casualties[0]}
GaulArmy = {'Army Size': ArmySize[1], "Positioning Value": positioning[1], 'Combat Quality': CombatPerformance[1],
                'Total Combat Value': CombatOutput[1], 'Name': 'The Gallic Army', 'Casualties': casualties[1]}

battle_occurring = True
new_round = True
day = 0

print(f"The starting strength of the Roman army was {RomeArmy['Army Size']} men")
print(f"The starting strength of the Gallic army was {GaulArmy['Army Size']} men")
print("____________________________________________")

while battle_occurring == True:


    while new_round == True:
        #RomeArmy = {'Army Size': ArmySize[0], "Positioning Value": positioning[0],
                    #'Combat Quality': CombatPerformance[0],
                    #'Total Combat Value': CombatOutput[0], 'Name': 'The Roman Army', 'Casualties': casualties[0]}
        #GaulArmy = {'Army Size': ArmySize[1], "Positioning Value": positioning[1],
                    #'Combat Quality': CombatPerformance[1],
                    #'Total Combat Value': CombatOutput[1], 'Name': 'The Gallic Army', 'Casualties': casualties[1]}
        day += 1
        # "Dice roll" function
        positioning = [random.randint(1, 6), random.randint(1, 6)]

        CombatPerformance = [(random.randint(1, 6) * positioning[0]), (random.randint(1, 6) * positioning[1])]

        RomeArmy['Total Combat Value'] = RomeArmy['Army Size'] * RomeArmy['Combat Quality']
        GaulArmy['Total Combat Value'] = GaulArmy['Army Size'] * GaulArmy['Combat Quality']

        print(f"The strength of the Roman army on day {day} was {RomeArmy['Army Size']} men")
        print(f"The strength of the Gallic army on day {day} was {GaulArmy['Army Size']} men")
        print("____________________________________________")

        if RomeArmy['Positioning Value'] > GaulArmy['Positioning Value']:
            print(f"Rome had the positioning advantage, equal to "
                  f"{RomeArmy['Positioning Value'] / GaulArmy['Positioning Value']}")
        elif GaulArmy['Positioning Value'] > RomeArmy['Positioning Value']:
            print(f"Gaul had the positioning advantage, equal to "
                  f"{GaulArmy['Positioning Value'] / RomeArmy['Positioning Value']}")
        else:
            print("The armies were equally well-positioned")

        print(f"The quality of the Roman performance was equal to {RomeArmy['Combat Quality']}")
        print(f"The quality of the Gallic performance was equal to {GaulArmy['Combat Quality']}")
        print("____________________________________________________")

        print(f"Roman Combat Output Quantity = "
              f"{RomeArmy['Total Combat Value']} ( {RomeArmy['Army Size']} men * {RomeArmy['Combat Quality']} )")
        print(f"Gallic Combat Output Quantity =  "
              f"{GaulArmy['Total Combat Value']} ( {GaulArmy['Army Size']} men * {GaulArmy['Combat Quality']})")
        #print("__________________________________________________________________________________________________")

        RomeArmy = {'Army Size': ArmySize[0], "Positioning Value": positioning[0],
                    'Combat Quality': CombatPerformance[0],
                    'Total Combat Value': CombatOutput[0], 'Name': 'The Roman Army', 'Casualties': casualties[0]}
        GaulArmy = {'Army Size': ArmySize[1], "Positioning Value": positioning[1],
                    'Combat Quality': CombatPerformance[1],
                    'Total Combat Value': CombatOutput[1], 'Name': 'The Gallic Army', 'Casualties': casualties[1]}

        #Rome Victory Case
        if RomeArmy['Total Combat Value'] > GaulArmy['Total Combat Value']:
            victor = RomeArmy['Name']
            RomeArmy['Casualties'] = abs((RomeArmy['Total Combat Value'] -
                                         GaulArmy['Total Combat Value']) / RomeArmy['Combat Quality'])
            GaulArmy['Casualties'] = abs((GaulArmy['Total Combat Value'] -
                                         RomeArmy['Total Combat Value']) / GaulArmy['Combat Quality'])
            RomeArmy['Army Size'] = RomeArmy['Army Size'] - RomeArmy['Casualties']

            if GaulArmy['Casualties'] > GaulArmy['Army Size']:
                GaulArmy['Casualties'] = GaulArmy['Army Size']
                GaulArmy['Army Size'] = GaulArmy['Army Size'] - GaulArmy['Casualties']
            else:
                GaulArmy['Army Size'] = GaulArmy['Army Size'] - GaulArmy['Casualties']

            print(f"{victor} is the victor. ")
            print(f"Roman casualties: {int(RomeArmy['Casualties'])} men")
            print(f"Gallic casualties: {int(GaulArmy['Casualties'])} men; ")
            print(f"Roman men remaining: {int(RomeArmy['Army Size'])}")
            print(f"Gallic men remaining: {int(GaulArmy['Army Size'])}")

        #Gaul Victory Case
        elif GaulArmy['Total Combat Value'] > RomeArmy['Total Combat Value']:
            victor = GaulArmy['Name']
            RomeArmy['Casualties'] = abs((RomeArmy['Total Combat Value'] -
                                         GaulArmy['Total Combat Value']) / RomeArmy['Combat Quality'])
            GaulArmy['Casualties'] = abs((GaulArmy['Total Combat Value'] -
                                          RomeArmy['Total Combat Value']) / GaulArmy['Combat Quality'])

            GaulArmy['Army Size'] = GaulArmy['Army Size'] - GaulArmy['Casualties']

            if RomeArmy['Casualties'] > RomeArmy['Army Size']:
                RomeArmy['Casualties'] = RomeArmy['Army Size']
                RomeArmy['Army Size'] = 0
            else:
                RomeArmy['Army Size'] = RomeArmy['Army Size'] - RomeArmy['Casualties']

            print(f"{victor} is the victor. ")
            print(f"Gallic casualties: {int(GaulArmy['Casualties'])} men; ")
            print(f"Roman casualties: {int(RomeArmy['Casualties'])} men")
            print(f"Gallic men remaining: {int(GaulArmy['Army Size'])}")
            print(f"Roman men remaining: {int(RomeArmy['Army Size'])}")

        #Draw Case
        else:
            victor = "on neither side"
            print("The battle was a draw")
            print(f"The victor was {victor}")
            RomeArmy['Casualties'] = abs((RomeArmy['Total Combat Value'] -
                                         GaulArmy['Total Combat Value']) / RomeArmy['Combat Quality'])
            GaulArmy['Casualties'] = abs((GaulArmy['Total Combat Value'] -
                                          RomeArmy['Total Combat Value']) / GaulArmy['Combat Quality'])

            GaulArmy['Army Size'] = GaulArmy['Army Size'] - GaulArmy['Casualties']

            if RomeArmy['Casualties'] > RomeArmy['Army Size']:
                RomeArmy['Casualties'] = RomeArmy['Army Size']
                RomeArmy['Army Size'] = 0
            else:
                RomeArmy['Army Size'] = RomeArmy['Army Size'] - RomeArmy['Casualties']
            if GaulArmy['Casualties'] > GaulArmy['Army Size']:
                GaulArmy['Casualties'] = GaulArmy['Army Size']
                GaulArmy['Army Size'] = GaulArmy['Army Size'] - GaulArmy['Casualties']
            else:
                GaulArmy['Army Size'] = GaulArmy['Army Size'] - GaulArmy['Casualties']


        if RomeArmy['Army Size'] or GaulArmy['Army Size'] <= 0:
            new_round = False
            battle_occurring = False
        #elif GaulArmy['Army Size'] <= 0:
             #new_round = False
             #battle_occurring = False
        else:
            new_round = True








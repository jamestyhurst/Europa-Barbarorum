import random

EconomicOutput = [random.randint(1,1000), random.randint(1,1000)]
ProductionModifier = [random.randint(1,10), random.randint(1,10)]
ProductionOutput = [EconomicOutput[0]*ProductionModifier[0], EconomicOutput[1]*ProductionModifier[1]]

Faction1 = {'name': 'Rome', 'Economy': EconomicOutput[0], 'Production Modifier': ProductionModifier[0],
            'Production Output': ProductionOutput[0]}
Faction2 = {'name': 'Gaul', 'Economy': EconomicOutput[1], 'Production Modifier': ProductionModifier[1],
            'Production Output': ProductionOutput[1]}

#print(Faction1)
#print(Faction2)

print("The Roman economic output was equal to", Faction1['Economy'], "Sesterses")
print("The Roman production modifier was equal to", Faction1['Production Modifier'], "out of 10")
print("Total Roman production was equal to", Faction1['Production Output'])
print("")
print("The Gallic economic output was equal to", Faction2['Economy'], "Sesterses")
print("The Gallic production modifier was equal to", Faction2['Production Modifier'], "out of 10")
print("Total Gallic production was equal to", Faction2['Production Output'])
print("                                                                                  ")

print("The armies of Rome and Gaul met in the field")
Attacker = random.randint(1, 2)
if Attacker ==1:
    print("Rome was the attacker")
else:
    print("Gaul was the attacker")
print("A battle occurred between the two armies; The fighting was bitter, the loser resisting to the last man.")
print("______________________")

ArmySize = [Faction1['Production Output'], Faction2['Production Output']]

# "Dice roll" function
positioning = [random.randint(1, 6), random.randint(1, 6)]

CombatPerformance = [(random.randint(1, 6)*positioning[0]), (random.randint(1, 6)*positioning[1])]

CombatOutput = [(ArmySize[0]*CombatPerformance[0]), (ArmySize[1]*CombatPerformance[1])]

RomeArmy = {'Army Size': ArmySize[0], "Positioning Value": positioning[0], 'Combat Quality': CombatPerformance[0],
            'Total Combat Value': CombatOutput[0]}
GaulArmy = {'Army Size': ArmySize[1], "Positioning Value": positioning[1], 'Combat Quality': CombatPerformance[1],
            'Total Combat Value': CombatOutput[1]}

print("The starting strength of the Roman army was", RomeArmy['Army Size'], "men")
print("The starting strength of the Gallic army was", GaulArmy['Army Size'], "men")
print("____________________________________________")

if positioning[0] > positioning[1]:
    print("Rome had the positioning advantage, equal to", positioning[0]/positioning[1])
elif positioning[0] < positioning[1]:
    print("Gaul had the positioning advantage, equal to", positioning[1]/positioning[0])
else:
    print("The armies were equally well-positioned")

print("The quality of the Roman performance was equal to", RomeArmy['Combat Quality'])
print("The quality of the Gallic performance was equal to", GaulArmy['Combat Quality'])
print("____________________________________________________")

print("Roman Combat Output Quantity =", RomeArmy['Total Combat Value'],
      "(", RomeArmy['Army Size'], "men *", RomeArmy['Combat Quality'], ")")
print("Gallic Combat Output Quantity =", GaulArmy['Total Combat Value'],
      "(", GaulArmy['Army Size'], "men *", GaulArmy['Combat Quality'], ")")
print("__________________________________")

if RomeArmy['Total Combat Value'] > GaulArmy['Total Combat Value']:
    victor =str(RomeArmy)
    RomeArmy['Army Size'] = RomeArmy['Army Size']\
                            - ((RomeArmy['Total Combat Value'] - GaulArmy['Total Combat Value']) / RomeArmy['Combat Quality'])
    print("Rome is the victor")
    print("Roman casualties were equal to",
          int((RomeArmy['Total Combat Value'] - GaulArmy['Total Combat Value']) / RomeArmy['Combat Quality']), "men")
    print("The Roman army size is now", int(RomeArmy['Army Size']), "men")
elif GaulArmy['Total Combat Value'] > RomeArmy['Total Combat Value']:
    victor = str(GaulArmy)
    GaulArmySize = GaulArmy['Army Size'] - ((GaulArmy['Total Combat Value'] -RomeArmy['Total Combat Value'])/GaulArmy['Combat Quality'])
    print("Gaul is the victor")
    print("Gallic casualties were equal to",
          int((GaulArmy['Total Combat Value'] - RomeArmy['Total Combat Value'])/GaulArmy['Combat Quality']), "men")
    print("The Gallic army size is now", int(GaulArmySize), "men")
else:
    victor = "neither"
    print("The battle was a draw")

print("The victor was", victor)



## Europa Barbarorum: In it's simplest form, a turn based strategy game. The theme is Roman era Europe, so that one
# can embrace barbarian gameplay

import random

EconomicOutput = [random.randint(1,1000), random.randint(1,1000)]
ProductionModifier = [random.randint(1,10), random.randint(1,10)]
ProductionOutput = [EconomicOutput[0]*ProductionModifier[0], EconomicOutput[1]*ProductionModifier[1]]

print("The Roman economic output was equal to", EconomicOutput[0], "Sesterses")
print("The Roman production modifier was equal to", ProductionModifier[0], "out of 10")
print("")
print("The Gallic economic output was equal to", EconomicOutput[1], "Sesterses")
print("The Gallic production modifier was equal to", ProductionModifier[1], "out of 10")
print("                                                                                  ")
print("The armies of Rome and Gaul met in the field")
print("A battle occurred between the two armies; The fighting was bitter, the loser resisting to the last man.")
print("______________________")

Attacker = random.randint(1, 2)
if Attacker ==1:
    print("Rome was the attacker")
else:
    print("Gaul was the attacker")

ArmySize = [(ProductionOutput[0]), (ProductionOutput[1])]
RomeArmySize = ArmySize[0]
GaulArmySize = ArmySize[1]

print("The starting strength of the Roman army was", RomeArmySize, "men")
print("The starting strength of the Gallic army was", GaulArmySize, "men")
print("____________________________________________")

positioning = [random.randint(1, 6), random.randint(1, 6)]
if positioning[0] > positioning[1]:
    print("Rome had the positioning advantage, equal to", positioning[0]/positioning[1])
else:
    print("Gaul had the positioning advantage, equal to", positioning[1]/positioning[0])


# "Dice roll" function
CombatPerformance = [(random.randint(1, 6)*positioning[0]), (random.randint(1, 6)*positioning[1])]
RomeCombatPerformance = CombatPerformance[0]
GaulCombatPerformance = CombatPerformance[1]
print("The quality of the Roman performance was equal to", RomeCombatPerformance)
print("The quality of the Gallic performance was equal to", GaulCombatPerformance)
print("____________________________________________________")


CombatOutput = [(ArmySize[0]*CombatPerformance[0]), (ArmySize[1]*CombatPerformance[1])]
RomeCombatOutput = CombatOutput[0]
GaulCombatOutput = CombatOutput[1]

print("Roman Combat Output Quantity =", RomeCombatOutput, "(", RomeArmySize, "men *", RomeCombatPerformance, ")")
print("Gallic Combat Output Quantity =", GaulCombatOutput, "(", GaulArmySize, "men *", GaulCombatPerformance, ")")
print("__________________________________")

if RomeCombatOutput > GaulCombatOutput:
    victor = RomeCombatOutput
    RomeArmySize = RomeArmySize - ((RomeCombatOutput - GaulCombatOutput) / RomeCombatPerformance)
    print("Rome is the victor")
    print("Roman casualties were equal to", int((RomeCombatOutput - GaulCombatOutput) / RomeCombatPerformance), "men")
    print("The Roman army size is now", int(RomeArmySize), "men")
elif GaulCombatOutput > RomeCombatOutput:
    victor = GaulCombatOutput
    GaulArmySize = GaulArmySize - ((GaulCombatOutput-RomeCombatOutput)/GaulCombatPerformance)
    print("Gaul is the victor")
    print("Gallic casualties were equal to", int((GaulCombatOutput - RomeCombatOutput)/GaulCombatPerformance), "men")
    print("The Gallic army size is now", int(GaulArmySize), "men")
else:
    print("The battle was a draw")





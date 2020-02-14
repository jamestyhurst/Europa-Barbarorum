#"Duel" series of code files: Duel1
# Purpose: for modeling combat between individual soldiers , to either simplify what was being attempted in the
# "Combat" series, or to use this code to model at the micro-scale the individual clashes that comprise a battle
# between armies as whole units



class Soldier:

    def __init__(self, health, armor, damage):
        self.health = health
        self.armor = armor
        self.damage = damage

    def attack(self, attacker, defender):
        self.attacker = attacker
        self.defender = defender
        defender.health = defender.health - attacker.damage

    def trade_blows(self, opponent1, opponent2):
        self.opponent1 = opponent1
        self.opponent2 = opponent2
        opponent1.health = opponent1.health - opponent2.damage
        opponent2.health = opponent2.health - opponent1.damage

Soldier1 = Soldier(100, 10, 12)
Soldier2 = Soldier(100, 12, 10)

print(Soldier.__dict__)
print(Soldier1.__dict__)
print(Soldier2.__dict__)

Soldier1.trade_blows(Soldier1, Soldier2)

print(Soldier1.__dict__)
print(Soldier2.__dict__)

#duel == True

while Soldier1.health and Soldier2.health > 0:

    print("(Soldier 1)")
    print("Make a decision")
    print("(1) Attack")
    x = input("")
    print(x)
    if x == "1":
        Soldier1.trade_blows(Soldier1, Soldier2)
        print(Soldier1.health, Soldier2.health)
    else:
        print("Error, please try again")

if Soldier1.health <= 0:
    Soldier1.health = 0
    print(Soldier1.health , Soldier2.health)
    print("Soldier 2 is victorious")
else:
    Soldier2.health = 0
    print(Soldier1.health, Soldier2.health)
    print("Soldier 1 is victorious")

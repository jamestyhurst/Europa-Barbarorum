from Season import *


class Test_Class:
    def __init__(self, provinces = None):
        if provinces is None:
            self.provinces = []
        else:
            self.provinces = provinces

    def add_province(self, province):
        if province not in self.provinces:
            self.provinces.append(province)

    def improve_province(self, province):
        if province in self.provinces:
            province['income'] = province['income'] * 2

    def grow_province(self, province):
        if province in self.provinces:
            province['population'] = province['population'] * 1.05

    def manage_province(self, province):
        action_loop = True
        while action_loop == True:
            print("Select a Province-Option")
            print("[1] Improve Income")
            print("[2] Grow Population")
            print("[3] Return to Turn Menu")
            province_choice = input()
            if province_choice == '1':
                self.improve_province(province)
                action_loop = False
                global turn
                turn = turn + 1
                season.change_season()
                #test_object.earn_province_income(test_object.provinces)
            elif province_choice == '2':
                self.grow_province(province)
                action_loop = False
                turn = turn + 1
                season.change_season()
                #test_object.earn_province_income(test_object.provinces)
            elif province_choice == '3':
                action_loop = False

            else:
                print("Please Try Again")


province1 = {'income': 10, 'population': 100}
test_object = Test_Class(None)
test_object.add_province(province1)
print(province1['income'])

#test_object.manage_province(province1)

print(province1['income'], province1['population'])



session_running = True
turn = 1
action_taken = False

season = Season('Spring', 1)
print(f"{season.name}, turn {turn}" )

while session_running:

    print(f"{season.name}, turn {turn}")
    #print(f"{faction1.treasury} denarii")
    print("Make Your Turn Decision")
    print("[1] Print Faction Information")
    print("[2] Print Province Information")
    print("[3] Upgrade Province")
    turn_choice = input()
    if turn_choice == '1':
        print(test_object)
    elif turn_choice == '2':
        print(province1)
    elif turn_choice == '3':

        test_object.manage_province(province1)

    else:
        print("Sorry, please try again")
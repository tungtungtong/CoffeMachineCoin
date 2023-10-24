import data
import logo

# MENU
menu = data.MENU
# COFFEE NAME
menu_list = data.MENU_LIST
# RESOURCE
resource = data.resources
# Payout Coins
payout_coin = data.payout_coin
# Insert Coins
insert_coin = data.insertCoin
# Profit
profit = 0
# Coffee name
coffee_name = ""
#
user_selection = 1

ingredients_water = 0
ingredients_milk = 0
ingredients_coffee = 0

for key in resource:
    resource_water = resource[key]
    resource_milk = resource[key]
    resource_coffee = resource[key]


# check machine have enough coin to payback
def paycheck():
    insert_coin500 = int(input("Number of 500coins: "))
    insert_coin100 = int(input("Number of 100coins: "))
    insert_coin50 = int(input("Number of 50coins: "))
    insert_coin10 = int(input("Number of 10coins: "))

    total = insert_coin500 * 500 + insert_coin100 * 100 + insert_coin50 * 50 + insert_coin10 * 10
    cost = menu[coffee_name]["cost"]

    if total >= cost:
        return True
    else:
        return False


# check machine have enough resource to make a coffe
def resource_check(coffee_number):
    global coffee_name
    global ingredients_water
    global ingredients_milk
    global ingredients_coffee

    coffee_name = menu_list[coffee_number]
    ingredients_coffee = menu[coffee_name]["ingredients"]["coffee"]
    ingredients_milk = menu[coffee_name]["ingredients"]["milk"]
    ingredients_water = menu[coffee_name]["ingredients"]["water"]

    if (resource_water >= ingredients_water and
            resource_milk >= ingredients_milk and
            resource_coffee >= ingredients_coffee):
        return True
    else:
        return False


# Make coffe after check resource
def coffee_make():
    global resource_coffee
    global resource_milk
    global resource_water

    resource_milk = resource_milk - ingredients_milk
    resource_coffee = resource_coffee - ingredients_coffee
    resource_water = resource_water - ingredients_water


def menu_print():
    print(logo.logo)
    print("______________________________________________")
    print("|    Select your action                      |")
    print("|    1. Order Coffee                         |")
    print("|    2. Report about resource                |")
    print("|    3. Report about coin in coffee machine  |")
    print("|    4. Report about profit                  |")
    print("|    0. Done                                 |")
    print("|____________________________________________|")
    menu_number = int(input("Your selection: "))
    if menu_number > 0:
        return menu_number
    else:
        print("Done")
        return 0


def cash_back():
    is_cash_back = True
    return is_cash_back


def coffe_menu():
    print(logo.logo)
    print("______________________________________________")
    print("|    Select your action                      |")
    print("|    1. Espresso                             |")
    print("|    2. Latte                                |")
    print("|    3. Cappuccino                           |")
    print("|    0. Return                               |")
    print("|____________________________________________|")
    coffee_number = int(input("Your selection: "))
    return coffee_number


def resource_report():
    print(f"Water: {resource_water}")
    print(f"Milk: {resource_milk}")
    print(f"Coffee: {resource_coffee}")


# Menu selection
def select_menu(menu_no):
    while menu_no > 0:
        if menu_no == 1:
            coffee_number = coffe_menu()
            if coffee_number == 0:
                break
            
            if resource_check(coffee_number):
                if paycheck():
                    coffee_make()
                    cash_back()
                else:
                    print("Not enough coins to payout")
            else:
                print("Not enough resource")
        elif menu_no == 2:
            resource_report()
        elif menu_no == 3:
            for key in payout_coin:
                print(f"{key}: {payout_coin[key]}")
        elif menu_no == 4:
            print(f"Profit: {profit}")
    if menu_no == 0:
        print("Done")


"""Start program"""
# Coffe Machine Run
while user_selection > 0:
    # Menu
    user_selection = menu_print()
    select_menu(user_selection)

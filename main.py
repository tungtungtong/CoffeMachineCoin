import time
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
insert_coin = 0
# Profit
profit = 0
# Coffee name
coffee_name = ""
# User selection
user_selection = 1
# Cost
cost = 0
# Payback
payback = 0
# Coffee material
ingredients_water = 0
ingredients_milk = 0
ingredients_coffee = 0
# Resource
resource_water = resource["water"]
resource_milk = resource["milk"]
resource_coffee = resource["coffee"]
# Payout Coin
payout500Coins = payout_coin["coins500"]
payout100Coins = payout_coin["coins100"]
payout50Coins = payout_coin["coins50"]
payout10Coins = payout_coin["coins10"]
# Insert Coins
insert_coin500 = 0
insert_coin100 = 0
insert_coin50 = 0
insert_coin10 = 0


# Check machine have enough coin to payback
def paycheck():
    global insert_coin, insert_coin500, insert_coin100, insert_coin50, insert_coin10, cost

    insert_coin500 = int(input("Number of 500coins: "))
    insert_coin100 = int(input("Number of 100coins: "))
    insert_coin50 = int(input("Number of 50coins: "))
    insert_coin10 = int(input("Number of 10coins: "))

    insert_coin = insert_coin500 * 500 + insert_coin100 * 100 + insert_coin50 * 50 + insert_coin10 * 10
    cost = menu[coffee_name]["cost"]

    time.sleep(1)
    print("\n")
    print(f"Total insert: {insert_coin}")
    print(f"Coffee price: {cost}")

    time.sleep(1)

    if insert_coin >= cost:
        return True
    else:
        return False


# check machine have enough resource to make a coffe
def resource_check(coffee_number):
    global coffee_name, ingredients_water, ingredients_milk, ingredients_coffee

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
    global resource_coffee, resource_milk, resource_water

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
    return menu_number


def coin_calculator(coin500, coin100, coin50, coin10):
    total = coin500 * 500 + coin100 * 100 + coin50 * 50 + coin10 * 10
    return  total


def cash_back():
    global payout500Coins, payout100Coins, payout50Coins, payout10Coins, insert_coin
    cash_back_500coins = 0
    cash_back_100coins = 0
    cash_back_50coins = 0
    cash_back_10coins = 0

    payout_cash = insert_coin - menu[coffee_name]["cost"]

    # Payout Coins Calculator
    payout500Coins += insert_coin500
    payout100Coins += insert_coin100
    payout50Coins += insert_coin50
    payout10Coins += insert_coin10

    # Print CashBack
    time.sleep(1)
    print(f"Your change: {payout_cash}")
    print("\n")
    time.sleep(1)

    # CashBack Coins Calculator
    while payout_cash > 0:
        if payout_cash >= 500 and payout500Coins > 0:
            payout_cash -= 500
            payout500Coins -= 1
            cash_back_500coins += 1
        elif payout_cash >= 100 and payout100Coins > 0:
            payout_cash -= 100
            payout100Coins -= 1
            cash_back_100coins += 1
        elif payout_cash >= 50 and payout100Coins > 0:
            payout_cash -= 50
            payout50Coins -= 1
            cash_back_50coins += 1
        else:
            payout_cash -= 10
            payout10Coins -= 1
            cash_back_10coins += 1

    time.sleep(1)
    print(f"Cashback 500Coins: {cash_back_500coins}")
    print(f"Cashback 100Coins: {cash_back_100coins}")
    print(f"Cashback 50Coins: {cash_back_50coins}")
    print(f"Cashback 10Coins: {cash_back_10coins}")


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
            break
        elif menu_no == 2:
            resource_report()
        elif menu_no == 3:
            for key in payout_coin:
                print(f"{key}: {payout_coin[key]}")
        elif menu_no == 4:
            print(f"Profit: {profit}")
    if menu_no == 0:
        print(logo.thankyou)


"""Start program"""
# Coffe Machine Run
while user_selection > 0:
    # Menu
    user_selection = menu_print()
    select_menu(user_selection)

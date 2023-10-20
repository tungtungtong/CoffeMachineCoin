import data
import logo

menu = data.MENU
menu_list = data.MENU_LIST
resource = data.resources
payout_coin = data.payout_coin
insert_coin = data.insertCoin
profit = 0
coffe_name = ""


# check machine have enough coin to payback
def paycheck():
    is_payout = True

    return is_payout


# check machine have enough resource to make a coffe
def resource_check(coffe_number):
    global coffe_name
    is_resource = True
    for key in menu_list:
        if key == coffe_number:
            coffe_name = menu_list[key]

    return is_resource


# Make coffe after check resource
def coffe_make():
    is_make_coffe = True

    print(logo.done)
    return is_make_coffe


def menu_print():
    print(logo.logo)
    print("______________________________________________")
    print("|    Select your action                      |")
    print("|    1. Order Coffe                          |")
    print("|    2. Report about resource                |")
    print("|    3. Report about coin in coffe machine   |")
    print("|    4. Report about profit                  |")
    print("|    0. Done                                 |")
    print("|____________________________________________|")
    menu_number = input("Your selection: ")
    return menu_number


def coffe_menu():
    print(logo.logo)
    print("______________________________________________")
    print("|    Select your action                      |")
    print("|    1. Espresso                             |")
    print("|    2. Latte                                |")
    print("|    3. Cappuccino                           |")
    print("|    0. Return                               |")
    print("|____________________________________________|")
    coffe_number = input("Your selection: ")
    return coffe_number


# Menu selection
def select_menu(menu_no):
    match menu_no:
        case "1":
            coffe_number = coffe_menu()
            if resource_check(coffe_number):
                if paycheck():
                    coffe_make()
                else:
                    print("Not enough coins to payout")
            else:
                print("Not enough resource")
        case "2":
            for key in resource:
                print(f"{key}: {resource[key]}")
        case "3":
            for key in payout_coin:
                print(f"{key}: {payout_coin[key]}")
        case "4":
            print(f"Profit: {profit}")
        case "0":
            print("Done")


"""Start program"""
# Menu
user_selection = menu_print()
# Coffe Machine Run
select_menu(user_selection)
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 800,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 750,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 950,
    },
}

print(MENU["latte"])

MENU_LIST = {
    "0": {"espresso"},
    "1": {"latte"},
    "2": {"cappuccino"},
}

resources = {
    "water": 3000,
    "milk": 2000,
    "coffee": 1500,
}

payout_coin = {
    "coins500": 15,
    "coins100": 15,
    "coins50": 15,
    "coins10": 15,
}

insertCoin = {
    "coins500": 0,
    "coins100": 0,
    "coins50": 0,
    "coins10": 0,
}
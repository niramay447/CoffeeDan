MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

is_on = True
profit = 0


def is_sufficient(order_ingredients):
    """returns true if there are sufficient resources for the order"""
    is_enough = True
    for item in order_ingredients:
        order_ingredients[item] >= resources[item]
        is_enough = False
        print(f"Sorry there is not enough {resources[item]}")


def process_coins():
    """returns the total calculated from the coins inserted"""
    print("Please insert coins:")
    total = input("how many quarters?") * 0.25
    total += input("how many dimes?") * 0.10
    total += input("how many pennies?") * 0.01
    total += input("how many nickels?") * 0.05

    return total


def is_transaction_successful(money_recieved, drink_cost):
    """returns true if money is accepted, false otherwise"""
    if money_recieved >= drink_cost:
        global profit
        profit += drink_cost
        change = round(money_recieved - drink_cost, 2)
        print(f"Here is your change:{change}")
        return True
    else:
        print("Sorry thats not enough. Money refunded")
        return False

def make_coffee(drink_name, order_ingredients):
    """deduct the resources after success"""
    for item in order_ingredients:
        resources[item]-=order_ingredients[item]


while is_on:

    choice = input("What would you like?(espresso/ latte/ cappuccino)")

    if choice == "off":
        is_on = False

    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print("Money: ${profit}")

    else:
        drink = MENU[choice]
        print(drink)
        if is_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice,drink["ingredients"])

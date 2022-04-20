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
    "water" : 300,
    "milk"  : 200,
    "coffee": 100,
    "money" : 0,
}
def ChechResources(OrderOfIngredients):
    for item in OrderOfIngredients:
        if OrderOfIngredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True
## quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
def CoinProcces(price):
    print("please insert coins.")
    total = int(input("how many quarters : "))*.25
    total += int(input("dimes : "))*.1
    total += int(input("nickles : "))*.05
    total += int(input("pennies : "))*.01
    if total < price :
        print("Sorry that's not enough money. Money refunded.")
        return False
    change = round(total - price,2)
    print(f"Here is ${change} dollars in change.")
    resources["money"] += price
    return True
def MakingDrink(Drink,Ingredients):
    for item in Ingredients:
        resources[item] -= Ingredients[item]
    print(f"Here is your {Drink}. Enjoy!")

while True:
    choice = input("What would you like? espresso/latte/cappuccino):")
    if choice == "off":
        break
    elif choice == "report":
        print("Water  : {} ml\nMilk   : {} ml\nCoffee : {} g\nMoney  : ${}".format(resources["water"],resources["milk"],resources["coffee"],resources["money"]))
    else:
        drink = MENU[choice]
        if ChechResources(drink["ingredients"]) == 0 :
            continue
        CoinProcces(drink["cost"])
        MakingDrink(choice,drink["ingredients"])

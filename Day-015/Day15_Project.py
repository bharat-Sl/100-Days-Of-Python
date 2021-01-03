#Project Day15

#clear terminal
#---------------------------------------------
import os
def clear():
    os.system('cls')
#---------------------------------------------

logo="""
  ___  __  ____  ____  ____  ____    _  _   __    ___  _  _  __  __ _ 
 / __)/  \(  __)(  __)(  __)(  __)  ( \/ ) / _\  / __)/ )( \(  )(  ( /
( (__(  O )) _)  ) _)  ) _)  ) _)   / \/ \/    \( (__ ) __ ( )( /    /
 \___)\__/(__)  (__)  (____)(____)  \_)(_/\_/\_/ \___)\_)(_/(__)\_)__)

"""

Menu={
    "espresso":{
        "ingredients":{
            "water":50,
            "coffee":18,
        },
        "cost":1.5
    },
    "latte":{
        "ingredients":{
            "water":200,
            "coffee":24,
            "milk":150,
        },
        "cost":2.5
    },
    "cappuccino":{
        "ingredients":{
            "water":250,
            "coffee":24,
            "milk":100,
        },
        "cost":3.0
    },
}

resources={
    "water": 300,
    "milk": 200,
    "coffee":100,
}

profit=0.0


def coffee_machine():
    global profit
    choice=input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice=='off':
        return 0
    elif choice=='report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}gm")
        print(f"Money: ${profit}")
    else:
        drink = Menu[choice]
        ingredients=drink["ingredients"]
        cost=drink["cost"]
        if(ingredients["water"]<=resources["water"] and ingredients["coffee"]<=resources["coffee"] and resources["milk"]<=resources["milk"]):
            print(f"{choice} cost ${cost}.")
            print("Please insert coins.")
            q=int(input("how many quarters?: "))
            d=int(input("how many dimes?: "))
            n=int(input("how many nickles?: "))
            p=int(input("how many pennies?: "))
            total=q*0.25+d*0.10+n*0.05+p*0.01
            change=round(total-cost,2)
            if(change<0): 
                print(f"Sorry that's not enough money. ${total} refunded.")
                input()
                return 1
            elif(change>0):
                profit+=cost
                print(f"Here is ${change} in change.")
                for item in ingredients:
                    resources[item] -= ingredients[item]
                print(f"Here is your {choice}. Enjoy!") 
                input()
                return 1
        else:
            print("Sorry, not enough ingredients.")
            input()
            return 1

on=True
while on:
    print(logo)
    check=coffee_machine()
    if(check==0):
        on=False
    clear()
    
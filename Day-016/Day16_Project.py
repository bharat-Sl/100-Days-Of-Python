#Project Day16

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

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


menu=Menu()
coffee_maker=CoffeeMaker()
money_machine=MoneyMachine()

on=True
while on:
    input("Enter to proceed.")
    clear()
    print(logo)
    choice=input(f"What would you like?({menu.get_items()}): ").lower()
    if(choice=="off"):
        on=False
        break
    elif(choice=="report"):
        coffee_maker.report()
        money_machine.report()
    else:
        item=menu.find_drink(choice)
        if(item=='None'):
            continue
        money=item.cost
        if(not coffee_maker.is_resource_sufficient(item)):
            continue
        if(not money_machine.make_payment(money)):
            continue
        coffee_maker.make_coffee(item)
        
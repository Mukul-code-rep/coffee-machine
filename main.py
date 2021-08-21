from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee = CoffeeMaker()
money_mac = MoneyMachine()

is_on=True

while is_on:
    ask = input(f"What would you like? {menu.get_items()} ")
    if ask == 'off':
        is_on = False
    elif ask.lower() == 'report':
        coffee.report()
        money_mac.report()
    else:
        drink = menu.find_drink(ask.lower())
        if coffee.is_resource_sufficient(drink) and money_mac.make_payment(drink.cost):
            coffee.make_coffee(drink)
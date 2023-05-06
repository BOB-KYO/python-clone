from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

#Program Requirements

#print report.
# money_machine = MoneyMachine()
# coffee_maker = CoffeeMaker()

# money_machine.report()
# coffee_maker.report()

#Check resurces sufficient?
# while is_on:
#     options = menu.get_items()
#     choice = input(f"What would you like? ({options}): ")
#     if choice == "off":
#         is_on = False
#     elif choice == "report":
#         money_machine.report()
#         coffee_maker.report()
#     else:
#         drink = menu.find_drink(choice)
#         print(drink)

#Process coins.
# is_enough_succesful = money_machine.make_payment(drink.cost)
#check transaction successful?
# is_enough_succesful = money_machine.make_payment(drink.cost)
#Make Coffee
# if is_enough_ingredients and is_enough_succesful:
#           coffee_maker.make_coffee(drink)

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True



while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink = menu.find_drink(choice)
        is_enough_ingredients = coffee_maker.is_resource_sufficient(drink)
        is_enough_succesful = money_machine.make_payment(drink.cost)
        if is_enough_ingredients and is_enough_succesful:
            coffee_maker.make_coffee(drink) # #1 option #This is easy to understanding and organized syntax  
        
        # if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
        #     coffee_maker.make_coffee(drink) #2 option

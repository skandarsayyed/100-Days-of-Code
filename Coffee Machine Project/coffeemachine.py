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

resources = { # machine resources
    "water": 300,
    "milk": 200,
    "coffee": 100,
    'money': 0,
}

def check_flavor(user_flavor):
    """CHECKS THE COFFEE FLAVOR"""
    for flavor in MENU:
        if user_flavor == flavor:
            menu_flavor = MENU[flavor]
            return menu_flavor
            
def check_resources(flavor_keys, machine_resources):
    """CHECKS IF THE RESOURCES ARE SUFFICIENT"""
    for key, required in flavor_keys['ingredients'].items():
        if key not in machine_resources or machine_resources[key] < required:
            print(f'Sorry there is not enough {key}.')
            return False
    return True

def check_coins():
    """CHECKS THE TOTAL COINS"""
    print('Please insert coins.')
    total = int(input('how many quarters? -> ')) * 0.25
    total += int(input('how many dimes? -> ')) * 0.1
    total += int(input('how many nickles? -> ')) * 0.05
    total += int(input('how many pennies? -> ')) * 0.01
    return total
            
def make_coffee(coffee_ingredients, machine_resources, coffee_cost, payment):
    """DEDUCTS RESOURCES FROM THE RESOURCES DICTIONARY AND ADD MONEY TO THE MONEY KEY IN THE RESOURCES DICTIONARY"""
    for resource in machine_resources:
        if resource in coffee_ingredients:
            machine_resources[resource] -= coffee_ingredients[resource]
        elif resource == 'money':
            transaction = round(payment - coffee_cost, 2)
            machine_resources[resource] += coffee_cost
            print(f'Here is your {transaction}$ in change.')
    return machine_resources

should_continue = True

while should_continue:
    # prompt the user
    # 'What do you like? (espresso/latte/cappuccino):'
    user_input = input('What do you like? (espresso/latte/cappuccino):')
    # check the user input
    if user_input in MENU:
        flavor_keys = check_flavor(user_flavor=user_input)
        bot_response = check_resources(flavor_keys=flavor_keys, machine_resources=resources)

        if bot_response == True:
            payment = check_coins()
            if payment >= flavor_keys['cost']:
                resources = make_coffee(coffee_ingredients=flavor_keys['ingredients'], machine_resources=resources, coffee_cost=flavor_keys['cost'], payment=payment)
                print(f'Here is your {user_input}. Enjoy!')
            else:
                print('Sorry, that is not enough money. Money refunded.')
        
    elif user_input == 'off': # to turn off the machine
        should_continue = False

    elif user_input == 'report': # to print the report
        print(f'{resources}')


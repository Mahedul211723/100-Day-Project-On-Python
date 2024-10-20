MENU = {
    "espresso": {
        "ingredients": {"water": 50, "coffee": 18},
        "cost": 1.5
    },
    "latte": {
        "ingredients": {"water": 200, "milk": 150, "coffee": 24},
        "cost": 2.5
    },
    "cappuccino": {
        "ingredients": {"water": 250, "milk": 100, "coffee": 24},
        "cost": 3.0
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100
}

def check_resources(drink):
    """Check if there are enough resources to make the drink."""
    for item in MENU[drink]["ingredients"]:
        if resources[item] < MENU[drink]["ingredients"][item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

def process_coins():
    """Process the coins inserted by the user and return the total amount."""
    print("Inserted Coins")
    
    for choice in MENU:
        cost = MENU[choice]["cost"]  # Correct case for "cost"
        print(f"The {choice} costs ${cost:.2f}")

    quarters = int(input("How many quarters(0.25$)? ")) * 0.25  # Fixed value
    dimes = int(input("How many dimes(0.10$)?")) * 0.10
    nickels = int(input("How many nickels(0.05$)? ")) * 0.05
    pennies = int(input("How many pennies(0.01$)? ")) * 0.01
    return quarters + dimes + nickels + pennies

def make_coffee(drink):
    """Deduct the ingredients from resources and add to profit."""
    for item in MENU[drink]["ingredients"]:
        resources[item] -= MENU[drink]["ingredients"][item]
    global profit
    profit += MENU[drink]["cost"]

is_on = True

while is_on:
    choice = input("What would you like? (espresso, latte, cappuccino): ").lower()
    
    if choice == 'off':
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Profit: ${profit:.2f}")  # Format profit for better readability
    elif choice in MENU:
        if check_resources(choice):
            payment = process_coins()
            if payment >= MENU[choice]["cost"]:
                change = payment - MENU[choice]["cost"]
                if change > 0:
                    print(f"Here is your change: ${change:.2f}")
                make_coffee(choice)
                print(f"Here is your coffee: {choice}. Enjoy!")
            else:
                print("That's not enough money! Money refunded.")
        else:
            continue
    else:
        print("Invalid choice. Please choose again.")

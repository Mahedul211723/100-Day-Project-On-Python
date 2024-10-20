#PIZZA ORDER
print('''    ____  
   .'    '.
    |  PIZZA  |
    |  ORDER  |
     '.___.__.'
        |  |
  +-----+--+-----+
  |     |  |     |
  |     |  |     |
  |  Crust   Toppings  |
  |     |  |     |
  +-----+--+-----+
        |  |
   +----+--+----+
   |  Size:      |
   |  Toppings:   |
   |  Quantity:   |
   |  Delivery:   |
   +--------------+
''')

print("Welcome to the Pizza Order")

size = input("Which size do you want? S, M, or L: ").strip().upper()
add_pepperoni = input("Do you want pepperoni? Y or N: ").strip().upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").strip().upper()
bill = 0

# Determine the base price of the pizza based on size
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25

# Add the cost of pepperoni if requested
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    elif size == "M":
        bill += 5
    elif size == "L":
        bill += 8

# Add the cost of extra cheese if requested
if extra_cheese == "Y":
    bill += 5

# Print the final bill
print(f"Your bill is ${bill}.")

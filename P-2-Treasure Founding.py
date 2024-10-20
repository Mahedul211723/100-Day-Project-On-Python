print('''
       *******************************************************************************"
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
  ''')     
     


print("\t\tWelcome to Treasure Island. Your mission is to find the treasure.")

# Get the player's choice of direction
direct = input("Which direction do you want to go? Right or Left: ").lower()

# Process the choice of direction
if direct == "left":
    # Get the player's choice of action (Swim or Wait)
    action = input("Do you want to Swim or Wait? ").lower()
    
    if action == "wait":
        # Get the player's choice of door
        door = input("Which door do you want to go through? Red, Blue, or Yellow: ").lower()
        
        if door == "red" or door == "blue":
            print("Game over. You chose the wrong door.")
        elif door == "yellow":
            print("Congratulations! You found the treasure!")
        else:
            print("Invalid choice. Game over.")
    
    elif action == "swim":
        print("Game over. You were eaten by a shark.")
    
    else:
        print("Invalid choice. Game over.")
    
elif direct == "right":
    print("Game over. You fell into a trap.")

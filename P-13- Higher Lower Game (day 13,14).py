import random
import os
import platform
import time  # Import the time module for adding delays

logo = """
  _    _ _       _                 _                            
 | |  | (_)     | |               | |                           
 | |__| |_  __ _| |__   ___ _ __  | |     _____      _____ _ __ 
 |  __  | |/ _` | '_ \ / _ \ '__| | |    / _ \ \ /\ / / _ \ '__|
 | |  | | | (_| | | | |  __/ |    | |___| (_) \ V  V /  __/ |   
 |_|  |_|_|\__, |_| |_|\___|_|    |______\___/ \_/\_/ \___|_|   
            __/ |                                               
           |___/                                                
"""

print(logo)

flowers_data = [
    {"name": "Ronaldo", "description": "Football star", "flower_count": 30, "country": "Portugal"},
    {"name": "Neymar", "description": "Football star", "flower_count": 25, "country": "Brazil"},
    {"name": "Shakira", "description": "Singer", "flower_count": 20, "country": "Colombia"},
    {"name": "Beyoncé", "description": "Singer", "flower_count": 50, "country": "USA"},
    {"name": "Taylor Swift", "description": "Singer", "flower_count": 45, "country": "USA"},
    {"name": "Lionel Messi", "description": "Football star", "flower_count": 35, "country": "Argentina"},
    {"name": "Ariana Grande", "description": "Singer", "flower_count": 40, "country": "USA"},
    {"name": "Cristiano Ronaldo", "description": "Football star", "flower_count": 60, "country": "Portugal"},
    {"name": "Selena Gomez", "description": "Singer", "flower_count": 32, "country": "USA"},
    {"name": "Jennifer Lopez", "description": "Singer/Actress", "flower_count": 33, "country": "USA"},
    {"name": "Bruno Mars", "description": "Singer", "flower_count": 28, "country": "USA"},
    {"name": "Katy Perry", "description": "Singer", "flower_count": 37, "country": "USA"},
    {"name": "Kanye West", "description": "Rapper", "flower_count": 22, "country": "USA"},
    {"name": "Drake", "description": "Rapper", "flower_count": 29, "country": "Canada"},
    {"name": "Eminem", "description": "Rapper", "flower_count": 31, "country": "USA"},
    {"name": "Rihanna", "description": "Singer", "flower_count": 27, "country": "Barbados"},
    {"name": "Ed Sheeran", "description": "Singer", "flower_count": 38, "country": "UK"},
    {"name": "Post Malone", "description": "Rapper/Singer", "flower_count": 41, "country": "USA"},
    {"name": "Adele", "description": "Singer", "flower_count": 49, "country": "UK"},
    {"name": "Billie Eilish", "description": "Singer", "flower_count": 42, "country": "USA"},
    {"name": "Justin Bieber", "description": "Singer", "flower_count": 43, "country": "Canada"},
]

def clear_console():
    """Clears the console screen."""
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

def random_pair():
    """Selects a random pair of items from the flowers_data."""
    return random.sample(flowers_data, 2)

def user_guess(item1, item2):
    """Prompts the user to guess which item has more flowers."""
    A = item1['flower_count']
    B = item2['flower_count']
    print(f"The description and country of {item1['name']} is {item1['description']} and {item1['country']}")
    print(f"The description and country of {item2['name']} is {item2['description']} and {item2['country']}")
    user_input = input(f"X. {item1['name']} Y. {item2['name']} - who has more flowers (Type X or Y)? ").strip().upper()
   
    if (user_input == 'X' and A > B) or (user_input == 'Y' and B > A):
        if user_input == 'X':
            print(f"{item1['name']} has more flowers with {A} flowers.")
        else:
            print(f"{item2['name']} has more flowers with {B} flowers.")
        
        print("Answer is correct")
        return True
    else:
        print("Wrong answer. Try again!")
        return False

def main():
    """Main game loop for the Higher Lower game."""
    is_game_over = False
    wrong_attempts = 0
    max_wrong_attempts = 3
    score = 0
    base_delay = 5  # Base delay time in seconds

    while not is_game_over:
        item1, item2 = random_pair()
        is_correct = user_guess(item1, item2)
        
        if is_correct:
            score += 1
            print(f"Your total points are {score}")
            wrong_attempts = 0  # Reset wrong attempts after a correct answer
        else:
            wrong_attempts += 1
            if wrong_attempts >= max_wrong_attempts:
                is_game_over = True
                print("Game Over! You have made too many wrong attempts.")
            else:
                # Increase delay based on the number of wrong attempts
                delay = base_delay * wrong_attempts
                print(f"Taking a break before the next question... ({delay} seconds)")
                time.sleep(delay)
        
        if not is_game_over:
            clear_console()

    print(f"Final Score: {score}")

if __name__ == "__main__":
    main()


import random
import os
import platform
logo='''/^^^     /^^                     /^^                               /^^^^                                                                                /^^       /^^/^^^^^^^^
/^ /^^   /^^                     /^^                             /^    /^^                                  /^                                          /^ /^^   /^^^/^^      
/^^ /^^  /^^/^^  /^^/^^^ /^^ /^^ /^^         /^^    /^ /^^^     /^^        /^^  /^^   /^^     /^^^^  /^^^^    /^^ /^^     /^^           /^^      /^^    /^^ /^^ / /^^/^^      
/^^  /^^ /^^/^^  /^^ /^^  /^  /^^/^^ /^^   /^   /^^  /^^        /^^        /^^  /^^ /^   /^^ /^^    /^^    /^^ /^^  /^^ /^^  /^^      /^^  /^^ /^^  /^^ /^^  /^^  /^^/^^^^^^  
/^^   /^ /^^/^^  /^^ /^^  /^  /^^/^^   /^^/^^^^^ /^^ /^^        /^^   /^^^^/^^  /^^/^^^^^ /^^  /^^^   /^^^ /^^ /^^  /^^/^^   /^^     /^^   /^^/^^   /^^ /^^   /^  /^^/^^      
/^^    /^ ^^/^^  /^^ /^^  /^  /^^/^^   /^^/^         /^^         /^^    /^ /^^  /^^/^            /^^    /^^/^^ /^^  /^^ /^^  /^^      /^^  /^^/^^   /^^ /^^       /^^/^^      
/^^      /^^  /^^/^^/^^^  /^  /^^/^^ /^^    /^^^^   /^^^          /^^^^^     /^^/^^  /^^^^   /^^ /^^/^^ /^^/^^/^^^  /^^     /^^           /^^   /^^ /^^^/^^       /^^/^^^^^^^^
                                                                                                                         /^^           /^^                                    '''
print(logo)
def clear_console():
    if platform.system() == 'Windows':
        os.system('cls') 
    else:
        os.system('clear')


def hard_level_game():
    secret_number = random.randint(1, 100)
    attempts_left = 5

    print("Welcome to the Number Guessing Game!")
    print("You have 5 attempts to guess the number between 1 and 100.")

    while attempts_left > 0:
        try:
            guess = int(input(f"You have {attempts_left} attempts left. Enter your guess: "))

            if guess == secret_number:
                print("Congratulations! You guessed the number correctly!")
                break
            elif guess < secret_number:
                print("Too low! Try again.")
            elif secret_number - 2 <= guess <= secret_number + 2:

                print("Around too close")
            else:
                print("Too high! Try again.")

            attempts_left -= 1

        except ValueError:
            print("Invalid input. Please enter an integer between 1 and 100.")
    if attempts_left == 0:
        print(f"Sorry, you've run out of attempts. The number was {secret_number}.")
def easy_level_game():
        secret_number = random.randint(1, 100)
        attempts_left = 10

        print("Welcome to the Number Guessing Game!")
        print("You have 10 attempts to guess the number between 1 and 100.")

        while attempts_left > 0:
            try:
                guess = int(input(f"You have {attempts_left} attempts left. Enter your guess: "))

                if guess == secret_number:
                    print("Congratulations! You guessed the number correctly!")
                    break
                elif guess < secret_number:
                    print("Too low! Try again.")
                elif secret_number - 2 <= guess <= secret_number + 2:

                    print("Around too close")
                else:
                    print("Too high! Try again.")

                attempts_left -= 1

            except ValueError:
                print("Invalid input. Please enter an integer between 1 and 100.")
        if attempts_left == 0:
            print(f"Sorry, you've run out of attempts. The number was {secret_number}.")
def main():
    input2 = input("Do you want to continue this game (yes, no): ").strip().lower()

    if input2 == 'yes':
        is_game_over = False
        while not is_game_over:
            input1 = input("Choose a Difficulty. Type 'easy' or 'hard': ").strip().lower()
            if input1 == 'hard':
                hard_level_game()
            elif input1 == 'easy':
                easy_level_game()
            else:
                print("Invalid choice. Please type 'easy' or 'hard'.")
            
            clear_console()
            
            # Example condition to end the game loop
            # is_game_over = True  # Uncomment this line to end the game after one iteration

    elif input2 == 'no':
        print("Game is over.")
    else:
        print("Invalid input. Please type 'yes' or 'no'.")

if __name__ == "__main__":
    main()
       
       
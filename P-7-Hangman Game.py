'''#Challenge a Picking Random word
word_list= ["addrvark","Watermillon","Babbon"]
import random
chosen_word=random.choice(word_list)
print(f"The random word is {chosen_word}")
guess=input("Guess a letter").lower()
for letter in chosen_word:
    if letter==guess:
        print("Right")
    else:
        print("Wrong")
        '''

#Picking Blank with Guesses
'''
import random
word_list = ["aardvark", "watermelon", "baboon"]
chosen_word = random.choice(word_list).lower() 
print(f"The random word is {chosen_word}")
display = ["_" for _ in range(len(chosen_word))]
print(display) 
guess = input("Guess a letter: ").lower()
for position in range(len(chosen_word)):
    letter = chosen_word[position]
    
    if letter == guess:
        display[position] = letter
print(display)
'''
#How to check if player is won
'''
import random
word_list = ["aardvark", "watermelon", "baboon"]
chosen_word = random.choice(word_list).lower() 
print(f"The random word is {chosen_word}")
display = ["_" for _ in range(len(chosen_word))]
print(display) 
end_of_game = False
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        
        if letter == guess:
            display[position] = letter
    print(" ".join(display))
    if "_" not in display:
        end_of_game = True
        print("You win!")
'''
#How To Kept Track Of player Lives
import random

stages = [
    '''
      +---+
      |   |
          |
          |
          |
          |
    =========''', 
    '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', 
    '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', 
    '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', 
    '''
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========''', 
    '''
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========''', 
    '''
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    ========='''
]

word_list = ["aardvark", "watermelon", "baboon"]
chosen_word = random.choice(word_list).lower() 
print(f"The random word is {chosen_word}")

display = ["_" for _ in range(len(chosen_word))]
print(" ".join(display))

lives = 6
end_of_game = False

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    
    if guess not in chosen_word:
        lives -= 1
    
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    
    print(" ".join(display))
    
    if "_" not in display:
        end_of_game = True
        print("You win!")
    
    if lives == 0:
        end_of_game = True
        print("You lose")
    
    print(stages[lives])

    
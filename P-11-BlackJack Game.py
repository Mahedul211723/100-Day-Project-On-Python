'''
import random
cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
random_usercards=random.sample(cards,2)
random_compuetercas=random.sample(cards,2)
total_sum=sum(random_usercards)
total_sum1=sum(random_compuetercas)
if random_usercards[0] or random_usercards[1]==cards[0]:
    print("User is won the game")
    if random_compuetercas[0] or random_compuetercas[1]==cards[0]:
        print("Compueter is won the game")  
    else:
        print("user is loss the game")
else:
    print("compueter is loss the game")
if total_sum>21:  
   input1= input("Do they have an ACE? Type 'yes'or 'no':")
   if input1=='yes':
     input2=input("If the ACE counts as a 1 instead of 11,are they still over 21?")
      '''
import random

# Define the deck of cards
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    """Returns a random card from the deck."""
    return random.choice(cards)

def calculate_score(hand):
    """Calculates the score of a given hand."""
    if sum(hand) == 21 and len(hand) == 2:
        return 0  # Blackjack
    if 11 in hand and sum(hand) > 21:
        hand.remove(11)
        hand.append(1)
    return sum(hand)

def compare(user_score, computer_score):
    """Compares the scores of the user and computer and returns the result."""
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "Lose, Opponent has Blackjack"
    elif user_score > 21:
        return "You went over. You lose."
    elif computer_score > 21:
        return "Opponent went over. You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose."

def play_game():
    """Play a game of Blackjack."""
    user_cards = []
    computer_cards = []
    is_game_over = False

    # Initial deal
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            should_continue = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if should_continue == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Computer's turn
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

def main():
    """Main function to start the game."""
    while True:
        play_game()
        if input("Do you want to play another game of Blackjack? Type 'yes' or 'no': ").lower() != 'yes':
            break

if __name__ == "__main__":
    main()

#Students Grade Problem
'''
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74  
}

student_grade = {}
for student in student_scores:
    score = student_scores[student]
    if score > 90:
        student_grade[student] = "Outstanding"
    elif score > 80:
        student_grade[student] = "Exceeds Expectations"
    elif score > 70:
        student_grade[student] = "Good"
    else:
        student_grade[student] = "Needs Improvement"  
for student in student_scores:
    score = student_scores[student]
    grade = student_grade[student]
    print(f"{student}: Score: {score}, Grade: {grade}")
'''


#Blind Auction Programe:

logo='''


                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\
                         `'-------'`
                       .-------------.
                   jgs/_______________\
 
                                     '''
'''
print(logo)
import os

bids = {}
bidding_finished = False

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder in bidding_record:
        bid_amount = float(bidding_record[bidder])  
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with a bid of ${highest_bid:.2f}")

while not bidding_finished:
    name = input("What is your Name? ").lower()
    price = input("What is your bid? $")
    bids[name] = price
    should_continue = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if should_continue == 'no':
        bidding_finished = True
        find_highest_bidder(bids)
    elif should_continue == 'yes':
        clear_console() 
    else:
        print("Please respond with 'yes' or 'no'.")
'''
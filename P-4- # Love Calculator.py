# Love Calculator
print('''    .-""""""-.
      .'          '.
     /   O      O   \
    :           `    :
    |                |   
    :    .------.    :
     \  '        '  /
      '.          .'
        '-......-'
    ''')

print("\t\tWelcome to the Love Calculator\t\t")

name1 = input("What is your name?: ").strip()
name2 = input("What is their name?: ").strip()

combined_string = name1 + name2
lower_case = combined_string.lower()

# Count occurrences of each letter in "TRUE" and "LOVE"
true_count = lower_case.count("t") + lower_case.count("r") + lower_case.count("u") + lower_case.count("e")
love_count = lower_case.count("l") + lower_case.count("o") + lower_case.count("v") + lower_case.count("e")

# Combine counts into a percentage
true_love = int(str(true_count) + str(love_count))

# Determine the message based on the love percentage
if true_love < 10 or true_love > 90:
    print(f"Your love percentage is {true_love}% and you together might like Coke and Mentos.")
elif 40 < true_love < 60:
    print(f"Your love percentage is {true_love}% and you together are alright.")
elif 20 <= true_love <= 40:
    print(f"Your love percentage is {true_love}% Go to normal but remember, everything is unpredictable.")
else:  # Handles the case where true_love is between 60 and 90 (non-inclusive)
    print(f"Your love percentage is {true_love}% and you may find it hard to find peace of mind.")


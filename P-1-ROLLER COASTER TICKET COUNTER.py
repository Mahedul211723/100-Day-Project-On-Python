#ROLLER COASTER TICKET COUNTER
'''
print("\t\t welcome to the Roller Coaster ticket counter\t\t")
hight=int(input("What is your hight in cm?:"))
age=int(input("Enter your age:"))
want_photos=input("Do you want to photos with your tikets?: Y or N ").strip().upper()
bill=0
if hight>=120:
    print("You can ride")
    if age<=12:
        bill+=5
        print("You Have to pay 5$")
    elif 12<age<=18:
        bill+=7
        print("You have to pay 7$")
    elif age>=18:
        bill+=12
        print("You have to pay 12$")
else:
    print("You Cant ride")

if want_photos=="Y":
    bill+=3
print(f"Your total bill for adding photo {bill}")
'''
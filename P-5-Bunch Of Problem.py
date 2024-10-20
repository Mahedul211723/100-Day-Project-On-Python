#LIFE IN WEEKS
'''
age=int(input("Enter your age:"))
passed_year=age
passed_day=age*365
passed_weeks=passed_year*52
years_remaining=90-age
days_remaining=years_remaining*365
month_remaining=years_remaining*12
weeks_remaining=years_remaining*52
print(f"you passed{passed_year}year in life")
print(f"you passed{passed_day}day in life")
print(f"you passed{passed_weeks}weeks in life")
print(f"years remaining is {years_remaining}")
print(f"days remaining is {days_remaining}")
print(f"month remaining is {month_remaining}")
print(f"weeks remaining is {weeks_remaining}")
'''
#TIPS CALCULATOR
'''
print("Welcome to the Tips calculator")
people=int(input("How many people in group?"))
bill=int(input("what was the total bill?$"))
tips=int(input("How much tips would you like to give?10,12,15"))
tips_as_percent=tips/100
total_tip_amount=bill*tips_as_percent
total_bill=bill+total_tip_amount
bill_per_person=total_bill/people
final_amount=round(bill_per_person)
print(f"Each person shiould pay:${final_amount}")
'''
#BMI CALCULATOR
'''
weight_in_kg=int(input("Enter your wight:"))
hight_in_m=float(input("Enter your hight:"))
bmi=(weight_in_kg/hight_in_m**2)
print(bmi)
bmi_as_int=int(bmi)
print(bmi_as_int)
'''
#Head Or Tail
'''
import random
test_Seed=int(input("create a seed number: "))
random.seed(test_Seed)
random_side=random.randint(0,1)
if random_side==1:
 print("Head")
else:
 print("Tail")
'''
#Randomly Choice person for paying bill
'''
import random
test_Seed=int(input("create a seed number: "))
random.seed(test_Seed)
name1=input("Give me everybodys name seperated by comma:")
names=name1.split(",")
person_who_will_pay=random.choice(names)
print(person_who_will_pay+"Go to buy the mill")
'''
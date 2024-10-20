#Function with outputs
'''
def format_name(f_name,l_name):
    print(f_name.title())
    print(l_name.title())
format_name("Mahedul","Islam")
'''
'''
def format_name(f_name,l_name):
    format_f_name=f_name.title()
    format_l_name=l_name.title()
    print(f"{format_f_name}{format_l_name}")
format_name("ANGLA","yu")
'''
#Leap_year month days problem
'''
def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def days_in_month(year, month):
    if month > 12 or month < 1:
        return "Invalid Input"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if month == 2 and is_leap(year):
        return 29
    return month_days[month - 1]
year = int(input("Enter the year: "))
month = int(input("Enter the month: "))

logo = '''      
_            _       _                 
___ __ _| | ___ _   _| | __ _| |_ ___  _ __ ___ 
  / __/ _` | |/ __| | | | |/ _` | __/ _ \\| '__/ __|
 | (_| (_| | | (__| |_| | | (_| | || (_) | |  \\__ \\
  \\___\\__,_|_|\\___|\\__,_|_|\\__,_|\\__\\___/|_|  |___/
'''

logo1 = '''
/ ,-----------------. \\
| |    1.05459 e -34| |
| `-----------------' |
| [@ ] On/Off  ###### |
|              ###### |
| [7] [8] [9] [C] [AC]| 
|                     |
| [4] [5] [6] [X] [%] |
|                     |
| [1] [2] [3] [+] [-] |
|                     |
| [0] [.]  [EXP]  [=] |
\\_____________________/
'''

print(logo)
print(logo1)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    num1 = float(input("What's the first number?: "))
    for symbol in operations:
        print(symbol)
        
    should_continue = True
    while should_continue:
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("What's the second number?: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        if input(f"Type 'y' to continue with {answer} or type 'n' to start a new calculation: ") == 'y':
            num1 = answer
        else:
            should_continue = False

calculator()



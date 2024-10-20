#Paint Area Calculator
'''
import math
def paint_case(hight,width,cover):
    area=hight*width
    num_of_cans=math.ceil(area/cover)
    print(f"Total cans is{num_of_cans} ")
hight=int(input("Enter The hight of the wall:"))
width=int(input("Enter the hight of the wall:"))
cover=5
paint_case(hight,width,cover)
'''

#Prime Number Calculator
'''
def prime_checker(number):
    is_prime=True
    for i in range(2,number-1):
       number%i==0
       is_prime=False
    if is_prime==True:  
      print("Its a prime Number")
    else:
          print("Its not a prime Number")     
number=int(input("Enter the number:"))  
prime_checker(number)         
'''
#Cypher Programe
'''
alphabate=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]     
direction=input("Type encode to encode your text and type decode to decode your text:")
text=input("Enter your text:")
shift=int(input("Enter the Shift number:\n"))
def encrypt(plain_text,shift_amount):
    cyper_text=[]
    for letter in plain_text:
        position=alphabate.index(letter)
        new_position=shift_amount+position
        new_letter=alphabate[new_position]
        cyper_text+=new_letter
    print(f"The encrypted text is:{(cyper_text)}")        
       
def decrypt(cyper_text,shift_amount):
    plain_text=[]
    for letter in cyper_text:
        position=alphabate.index(letter)
        new_position=position-shift_amount
        new_letter=alphabate[new_position]
        plain_text+=new_letter
    print(f"The decrypt text id {plain_text}")
if direction=="encode":
   encrypt(plain_text=text,shift_amount=shift)
elif direction=="decode":
    decrypt(cyper_text=text,shift_amount=shift)
else:
    print("Direction is wrong")
'''
#Ceaser Cipher Program in one function
'''
alphabate=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]     
def ceaser(start_text, shift_amount, cipher_directalphabate = ['a', 'b', 'cion):
    end_text = ""
    for letter in start_text:
        if letter in alphabate:
            position = alphabate.index(letter)
            if cipher_direction == "encode":
                new_position = (position + shift_amount) % len(alphabate)
            elif cipher_direction == "decode":
                new_position = (position - shift_amount) % len(alphabate)
            end_text += alphabate[new_position]
        else:
            end_text += letter 
    return end_text

direction = input("Type encode to encode your text and type decode to decode your text: ")
text = input("Enter your text: ")
shift = int(input("Enter the Shift number:\n"))

result = ceaser(start_text=text, shift_amount=shift, cipher_direction=direction)
print(f"The {direction} text is: {result}")
'''
#Ceaser Cipher Final Project
logo=  '''                                                           
           88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88 
              '''

print(logo)                                            
alphabate=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]     

def ceaser(start_text, shift_amount, cipher_direction):
    end_text = ""
    for char in start_text:
        if char in alphabate:
            position = alphabate.index(char)
            if cipher_direction == "encode":
                new_position = (position + shift_amount) % len(alphabate)
            elif cipher_direction == "decode":
                new_position = (position - shift_amount) % len(alphabate)
            end_text += alphabate[new_position]
        else:
            end_text += char 
    return end_text
should_continue=True
while should_continue:
 direction = input("Type encode to encode your text and type decode to decode your text: ")
 text = input("Enter your text: ")
 shift = int(input("Enter the Shift number:\n"))
 shift=shift%25
 print(shift)
 result = ceaser(start_text=text, shift_amount=shift, cipher_direction=direction)
 print(f"The {direction} text is: {result}")
 again=input("Type 'yes' if you want to go again otherwise type 'no'.\n")
 if again=='no':
     should_continue==False
     print("Goodbye")
    
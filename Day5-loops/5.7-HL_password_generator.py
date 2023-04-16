import string
import random
import sys

alphabet = string.ascii_lowercase
alphabet += string.ascii_uppercase
final_alphabet = []
numeric = []
s_symbol = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
password = []
#print(alphabet)
for i in alphabet:
   final_alphabet.append(i)

for i in range(0, 9):
   numeric.append(i)
   
#print(final_alphabet) 
#print(numeric)
#print(s_symbol)

letter = int(input("How many many letter would you like to have:"))
print()
if letter < 1:
    print("Invalid number of letters specified. Must be greater than 0")
    sys.exit(1)
number = int(input("How many many number would you like to have:"))
print()
if number < 1:
    print("Invalid number of numbers specified. Must be greater than 0")
    sys.exit(1)
symbol = int(input("symbol count"))
print()
if symbol < 1:
    print("Invalid number of symbol specified. Must be greater than 0")
    sys.exit(1)

for i in range(0, letter):
   pick_alphabet = random.choice(final_alphabet)
   password += pick_alphabet


for i in range(0, number):
   pick_numeric = random.choice(numeric)
   password.append(str(pick_numeric))
   

for i in range(0, symbol):
   pick_symbol = random.choice(s_symbol) 
   password.append(pick_symbol)

Final_password =[]

for i in password:
   Final_password.append(i)

print(Final_password)

random.shuffle(Final_password)

print(Final_password)

yy = "".join(Final_password)

print(f"your password is: {yy}")   





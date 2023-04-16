print("Welcome to the password generator")
import string
import random

alphabet = []
numeric = []
symbol = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
password = ""
xx = string.ascii_lowercase[:]
yy = string.ascii_uppercase[:]
#print(yy)
#print(xx)

for i in xx:
    alphabet.append(i)
for i in yy:
    alphabet.append(i)
for i in range(0,10):
    numeric.append(i)



#print(alphabet)    
#print(numeric)
#print(symbol)

password_lenght = int(input("How many letter would you like in your password?\n")) 
password_num = int(input("How many number would you like?\n"))
password_symbol = int(input("How many symbol would you like?\n"))

for i in range(1, password_lenght +1):
    password += random.choice(alphabet)

for i in range(1, password_num + 1):
    password += str(random.choice(numeric))

for i in range(1, password_symbol + 1):
    password += random.choice(symbol)

print(f"Here is your password {password}")

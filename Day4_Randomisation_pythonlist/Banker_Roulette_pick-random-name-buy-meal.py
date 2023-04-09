# Import the random module here
import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name_len =len(names_string.split(", "))
print(name_len - 1)
print(names)

random_pick = random.randint(0,name_len - 1)
print(random_pick)
print(f"{names[random_pick]} is going to buy the meal today!")

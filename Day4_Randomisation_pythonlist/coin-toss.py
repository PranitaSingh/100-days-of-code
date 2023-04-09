#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
	 
#Write the rest of your code below this line 👇
import random

input("Please click enter to Toss the coin")
coin_toss = random.randint(0,1)
if coin_toss == 0:
    print("Tails")
else:
    print("Heads")    

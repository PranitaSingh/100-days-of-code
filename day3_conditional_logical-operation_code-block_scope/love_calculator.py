# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name_lowercase = name1.lower() + name2.lower()
true_count = name_lowercase.count("t") + name_lowercase.count("r") + name_lowercase.count("u") +name_lowercase.count("e") 

love_count = name_lowercase.count("l") + name_lowercase.count("o") + name_lowercase.count("v") +name_lowercase.count("e")

score = int(str(true_count) + str(love_count))

if score < 10 and score > 90:
    print(f"Your score is {score},you go together like coke and mentos.")

elif score >= 40 and score <= 50:
    print(f"Your acore is {score}, you are alright together.") 

else:
    print(f"Your score is {score}") 

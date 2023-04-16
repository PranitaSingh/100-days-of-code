# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
years_left = 90 - int(age)
weeks = 52 * int(years_left)
months = 12 * int(years_left)
days = 365 * int(years_left)
print(f"You have {days} days, {weeks} weeks, and {months} months left.")

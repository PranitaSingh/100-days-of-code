print("Welcome to tip calculator")
bill = float(input("what was the total bill?"))
tip = int(input("what percentage of tip would you like to give? 10 , 12 or 15 ?"))
people_split_bill = int(input("How many people to split the bill?"))

tip_percentage_calculate = tip/100 * bill
total_bill = float(bill + tip_percentage_calculate)
bill_per_person = round(total_bill/people_split_bill,2)

print(f"each person should pay {bill_per_person}")




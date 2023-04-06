print("my Calculator")
op = input("what do you want to do ? A, M or S:")

if op == "A":
    first_num = int(input("Enter 1st num:"))
    second_num = int(input("Enter 2nd num:"))
    print(f"Result is {first_num + second_num}")
elif op == "S":
    first_num = int(input("Enter 1st num:"))
    second_num = int(input("Enter 2nd num:"))
    print(f"Result is {first_num - second_num}") 
elif op == "M":
    first_num = int(input("Enter 1st num:"))
    second_num = int(input("Enter 2nd num:"))
    print(f"Result is {first_num * second_num}") 
else:
    print("unsupported command. enter A, S or M")
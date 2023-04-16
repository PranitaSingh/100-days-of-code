Student_height = input("List of student height:\n").split()
total = 0
count = 0

for i in Student_height:
    print(i)
    count = count + 1
    total = total + int(i)
print(f"The sum is {total}")
print(f"The count is {count}")
print(f"The average is {total/count}")



student_score = input("input list of student score:").split()
print(student_score)
highest_score = 0
for i in student_score:
    score = int(i)
    print(score)
    if score > highest_score:
       highest_score = score

print(f"highest score is {highest_score}")       

    

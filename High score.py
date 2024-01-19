student_score = input().split()
for n in range(0, len(student_score)):
    student_score[n] = int(student_score[n])
high_score = 0
for score in student_score:
    if high_score < score:
        high_score = score


print(f"The highest score in the class is: {high_score}")

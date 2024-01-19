student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
total_height = 0
number_of_students = len(student_heights)
for i in student_heights:
    total_height += i

avg_height = round(total_height/number_of_students)
print(f"total height = {total_height}")
print(f"number of students = {number_of_students}")
print(f"average height = {avg_height}")
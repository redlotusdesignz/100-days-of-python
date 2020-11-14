
#calculating student heights without using len() or sum()

total = 0
counter = 0

student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  total = total + student_heights[n]
  counter+=1


height = round(total / counter)

print(height)



#determine the highest score without using the max() function

student_scores = input("Input a list of student scores\n ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])


max_score = 0

for s in student_scores:
  if s > max_score:
    max_score = s
print (f"\nThe highest score in class is {max_score}")

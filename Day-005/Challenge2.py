#challenge 2
student_scores = input("Input a list of student scores seperated by space:").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

heighest=0
#heighest=max(student_scores)
for score in student_scores:
    if(score>heighest):
        heighest=score
print(f"The highest score in the class is: {heighest}")
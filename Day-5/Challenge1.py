#challenge 1
student_heights = input("Input a list of student heights seperated by space:").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
  #sum+=student_heights[n]
sm=0
no_of_students=0
#sm=sum(student_heights)
for height in student_heights:
    no_of_students+=1
    sm=sm+height

print(f"Average height of students is {round(sm/no_of_students)}")
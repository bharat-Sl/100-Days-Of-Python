#challenge 2

from turtle import Turtle, Screen

the_turtle=Turtle()
the_turtle.color("Black")
# for i in range(50):
#     if i%2==0:
#         the_turtle.color("Black")
#     else:
#         the_turtle.color("White")
#     the_turtle.forward(10)

for i in range(50):
    the_turtle.forward(10)
    the_turtle.penup()
    the_turtle.forward(10)
    the_turtle.pendown()
screen=Screen()
screen.exitonclick()
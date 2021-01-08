#challenge 1

from turtle import Turtle, Screen

the_turtle=Turtle()
the_turtle.color("black")
for i in range(4):
    the_turtle.forward(100)
    the_turtle.left(90)
screen=Screen()
screen.exitonclick()
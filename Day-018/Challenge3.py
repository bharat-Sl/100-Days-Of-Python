#challenge 3

from turtle import Turtle, Screen
import random
the_turtle=Turtle()

for side in range(3,11):
    random_number = random.randint(0,16777215)
    hex_number = str(hex(random_number))
    hex_number ='#'+ hex_number[2:]
    the_turtle.color(hex_number)
    angle=(side-2)*180/side
    for i in range(0,side):
        the_turtle.forward(100)
        the_turtle.right(180-angle)

screen=Screen()
screen.exitonclick()
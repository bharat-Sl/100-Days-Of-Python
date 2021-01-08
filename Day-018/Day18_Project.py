#Project Day18
# import colorgram
# import os
# import sys

# rgb_colors = []
# colors = colorgram.extract(os.path.join(os.path.dirname(sys.argv[0]), 'image.jpg'), 30)
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     new_color=(r,g,b)
#     rgb_colors.append(new_color)
# print(rgb_colors)

import turtle as t
import random

t.colormode(255)
rgb_colors=[(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]
robot=t.Turtle()
robot.speed("fastest")
robot.hideturtle()
for i in range(10):
    robot.penup()
    robot.setpos(-300,-300+70*i)
    robot.pendown()
    for j in range(10):
        robot.color(random.choice(rgb_colors))
        robot.begin_fill()
        robot.circle(20)
        robot.end_fill()
        robot.penup()
        robot.forward(70)
        robot.pendown()
    robot.penup()
    robot.pendown()


screen=t.Screen()
screen.exitonclick()
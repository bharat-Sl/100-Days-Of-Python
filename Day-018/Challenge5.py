#challenge 5
import random
import turtle as t
robot=t.Turtle()
robot.speed("fastest")
robot.hideturtle()
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
for i in range(90):
    robot.color(random.choice(colours))
    robot.circle(100)
    robot.setheading(robot.heading()+4)


screen=t.Screen()
screen.exitonclick()
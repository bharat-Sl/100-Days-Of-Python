#challenge 4
import turtle as t
import random
t.colormode(255)
robot=t.Turtle()
robot.speed("fastest")
robot.width(6)
robot.hideturtle()
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
for i in range(150):
    robot.pencolor((random.randint(1,255),random.randint(1,255),random.randint(1,255)))
    random_choice= random.randint(1,99999)
    if(random_choice%4==0):
        robot.right(90)
    elif(random_choice%4==1):
        robot.left(90)
    elif(random_choice%4==2):
        robot.left(180)
    robot.forward(50)

screen=t.Screen()
screen.exitonclick()
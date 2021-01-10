#Project Day19
import turtle
import random
class mouse:
    def __init__(self,x,y,color):
        self.robot=turtle.Turtle()
        self.x_axis=x
        self.y_axis=y
        self.robot.shape("turtle")
        self.robot.shapesize(1.5)
        self.robot.color(color)
        self.robot.penup()
        self.robot.goto(x=self.x_axis,y=self.y_axis)

    def run(self):
        random_run=random.randint(7,20)
        self.x_axis+=random_run*5
        self.robot.forward(random_run)
    
def getUserInput(screen):
    return screen.textinput(
        title="Make your bet",
        prompt="Which turtle will win the race? Enter a color: "
    )
start=False
screen=turtle.Screen()
screen.setup(width=500,height=400)
turtles=[]
colours = ["violet","indigo","blue","green","yellow","orange","red"]
for i in range(7):
    turtles.append(mouse(-230,-150+i*50,colours[i]))
user_bet=getUserInput(screen)
if not user_bet:
    user_bet=getUserInput(screen)
else:
    start=True
while start:
    for turt in turtles:
        if turt.robot.xcor()>210:
            start=False
            color=turt.robot.fillcolor().lower()
            if color==user_bet.lower():
                print(f"You've won! The {color} turtle is the winner!")
            else:
                print(f"You've lost! The {color} turtle is the winner!")
        turt.run()
screen.exitonclick()


print(user_bet)
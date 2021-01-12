import turtle

class Crossy(turtle.Turtle):
    def __init__(self,screen):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.goto(0,-210)
        self.screen=screen
        self.setheading(90)
    
    def up(self):
        if(self.ycor()<260):
            self.forward(20)

    def move(self):
        self.screen.listen()
        self.screen.onkeypress(self.up,"Up")

    def reset(self):
        self.goto(0,-210)
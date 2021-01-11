import turtle

class Paddle(turtle.Turtle):
    def __init__(self,x_axis,screen):
        super().__init__()
        self.penup()
        self.x=x_axis
        self.shape("square")
        self.shapesize(stretch_len=5,stretch_wid=1)
        self.color("white")
        self.goto(self.x,0)
        self.screen=screen
        self.setheading(90)
    
    def up(self):
        if(self.ycor()<250):
            self.forward(25)

    def down(self):
        if(self.ycor()>-250):
            self.backward(25)

    def move(self,num):
        self.screen.listen()
        if(num==0):
            self.screen.onkeypress(self.up,"Up")
            self.screen.onkeypress(self.down,"Down")
        else:
            self.screen.onkeypress(self.up,"w")
            self.screen.onkeypress(self.down,"s")
            self.screen.update()

    def reset(self):
        self.goto(self.x,0)
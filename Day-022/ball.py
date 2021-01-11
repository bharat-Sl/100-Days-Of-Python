from turtle import Turtle
import time
import random

class Ball(Turtle):
    def __init__(self,screen):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.x_move=15
        self.y_move=15
        self.screen=screen
    def move(self):
        new_x=self.xcor()+self.x_move
        new_y=self.ycor()+self.y_move
        self.goto(new_x,new_y)
    
    def wall_bounce(self):
        self.y_move*=(-1)

    def block_bounce(self):
        self.x_move*=-1

    def reset(self):
        time.sleep(1)
        self.goto(0,0)
        self.screen.update()
        x=random.choice([-1,1])
        y=random.choice([-1,1])
        self.x_move=15*x
        self.y_move=15*y
        time.sleep(1)
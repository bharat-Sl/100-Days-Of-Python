import turtle
import random

class Food(turtle.Turtle):
    def __init__(self,screen):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.screen=screen
        self.shapesize(0.35)
        self.color("blue")
        self.speed("fastest")
        self.refresh()
    
    def refresh(self):
        random_x=random.randint(-28,28)*10
        random_y=random.randint(-28,28)*10
        self.goto(random_x,random_y)
        self.screen.update()
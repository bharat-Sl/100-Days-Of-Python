from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.penup()
        self.hideturtle()
        self.goto(-280,260)
        self.color("black")
        self.update()
    
    def increase_level(self):
        self.level+=1
        self.clear()
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",align="center",font=("Courier",40,"normal"))

    def update(self):
        self.write(f"Level {self.level}",align="left",font=("Courier",20,"normal"))
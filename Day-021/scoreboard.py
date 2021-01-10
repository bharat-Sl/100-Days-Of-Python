from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.hideturtle()
        self.goto(0,260)
        self.color("white")
        self.update()
    
    def increase_score(self):
        self.score+=1
        self.clear()
        self.update()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER",align="center",font=("Courier",30,"normal"))

    def update(self):
        self.write(f"Score:{self.score}",align="center",font=("Courier",24,"normal"))
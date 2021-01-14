from turtle import Turtle
import os
import sys

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.highscore=0
        with open(os.path.join(sys.path[0], "score.txt"), "r") as file:
            self.highscore=int(file.read())
        self.penup()
        self.hideturtle()
        self.goto(0,260)
        self.color("white")
        self.update()
    
    def increase_score(self):
        self.score+=1
        self.update()

    def reset(self):
        if self.score>self.highscore:
            with open(os.path.join(sys.path[0], "score.txt"), "w") as file:
                file.write(str(self.score))
            self.highscore=self.score
        self.score=0
        self.update()

    def update(self):
        self.clear()
        self.write(f"Score:{self.score} High Score:{self.highscore}",align="center",font=("Courier",24,"normal"))
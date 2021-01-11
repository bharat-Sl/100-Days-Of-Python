from turtle import Turtle

class Field(Turtle):

    def __init__(self):
        super().__init__()
        self.right_score=0
        self.left_score=0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.pensize(3)
        self.update()

    def increase_right_score(self):
        self.right_score+=1
        self.clear()
        self.update()

    def increase_left_score(self):
        self.left_score+=1
        self.clear()
        self.update()

    def game_over(self,left):
        self.goto(0,0)
        self.write(f"GAME OVER\n{left} wins",align="center",font=("Courier",30,"normal"))


    def update(self):
        print("updated")
        for i in range(-280,280,30):
            self.goto(0,i)
            self.pendown()
            self.goto(0,i+15)
            self.penup()
        self.goto(0,220)
        self.color("white")
        self.write(f"{self.left_score}   {self.right_score}",align="center",font=("Courier",48,"normal"))
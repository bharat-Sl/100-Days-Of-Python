import turtle
import time
from food import Food
from scoreboard import Scoreboard

class Snake:
    def __init__(self,screen):
        self.snake_body=[]
        self.screen=screen
        self.food=Food(screen)
        self.positions=[(0,0),(-10,0),(-20,0)]
        self.scoreboard=Scoreboard()
        for position in self.positions:
            self.add_body(position)
            self.screen.update()
    
    def up(self):
        if self.snake_body[0].heading()!=270:
            self.snake_body[0].setheading(90)
    def down(self):
        if self.snake_body[0].heading()!=90:
            self.snake_body[0].setheading(270)
    def left(self):
        if self.snake_body[0].heading()!=0:
            self.snake_body[0].setheading(180)
    def right(self):
        if self.snake_body[0].heading()!=180:
            self.snake_body[0].setheading(0)

    def snake_direction(self):
        self.screen.listen()
        self.screen.onkeypress(self.up,"Up")
        self.screen.onkeypress(self.down,"Down")
        self.screen.onkeypress(self.left,"Left")
        self.screen.onkeypress(self.right,"Right")
    

    def move(self):
        for seg_num in range(len(self.snake_body)-1,0,-1):
            new_x=self.snake_body[seg_num-1].xcor()
            new_y=self.snake_body[seg_num-1].ycor()
            self.snake_body[seg_num].goto(new_x,new_y)
        self.snake_body[0].forward(10)
    
    def add_body(self,position):
        body=turtle.Turtle("square")
        body.color("white")
        body.penup()
        body.shapesize(0.5)
        body.goto(position)
        self.snake_body.append(body)

    def increase(self):
        self.add_body(self.snake_body[-1].position())
    
    def play(self,check):
        self.snake_direction()
        while check:
            if self.snake_body[0].distance(self.food)<5:
                self.food.refresh()
                self.increase()
                self.scoreboard.increase_score()
            
            for body in self.snake_body[1::]:
                if self.snake_body[0]==body:
                    continue
                elif self.snake_body[0].distance(body)<5:
                    self.scoreboard.game_over()
                    check=False

            if self.snake_body[0].xcor()>290 or self.snake_body[0].xcor()<-290 or self.snake_body[0].ycor()>290 or self.snake_body[0].ycor()<-290:
                self.scoreboard.game_over()
                check=False
            self.move()
            time.sleep(0.1)
            self.screen.update()

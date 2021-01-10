#Project Day20
# snake part 1
import turtle
import time

class Snake:
    def __init__(self):
        self.snake_body=[]
        self.positions=[(0,0),(-10,0),(-20,0)]
        for position in self.positions:
            body=turtle.Turtle()
            body.color("white")
            body.penup()
            body.shape("square")
            body.shapesize(0.5)
            body.goto(position)
            screen.update()
            self.snake_body.append(body)
    
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
        screen.listen()
        screen.onkeypress(self.up,"Up")
        screen.onkeypress(self.down,"Down")
        screen.onkeypress(self.left,"Left")
        screen.onkeypress(self.right,"Right")
    

    def move(self):
        for seg_num in range(len(self.snake_body)-1,0,-1):
            new_x=self.snake_body[seg_num-1].xcor()
            new_y=self.snake_body[seg_num-1].ycor()
            self.snake_body[seg_num].goto(new_x,new_y)
        self.snake_body[0].forward(10)
    
    def play(self,check):
        self.snake_direction()
        while check:
            self.move()
            self.positions.insert(0,(int(self.snake_body[0].pos()[0]),int(self.snake_body[0].pos()[1])))
            del self.positions[-1]
            time.sleep(0.1)
            screen.update()


screen=turtle.Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake=Snake()
snake.play(True)









screen.mainloop()
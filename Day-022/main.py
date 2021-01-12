#Project Day22
import turtle
from field import Field
from paddle import Paddle
from ball import Ball
import time

screen=turtle.Screen()
screen.tracer(0)
screen.bgcolor("black")
screen.setup(800,600)
screen.title("Pong")

field=Field()
right_paddle=Paddle(350,screen)
left_paddle=Paddle(-350,screen)
ball=Ball(screen)

screen.update()
right_paddle.move(0)
left_paddle.move(1)
game_on=True
slep=0.1
while game_on:
    time.sleep(slep)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wall_bounce()
    if ball.distance(right_paddle)<50.97 and ball.xcor()>330:
        ball.block_bounce()
        slep*=0.9
    if ball.distance(left_paddle)<50.97 and ball.xcor()<-330:
        ball.block_bounce()
        slep*=0.9
    if ball.xcor() > 360:
        field.increase_right_score()
        left_paddle.reset()
        right_paddle.reset()
        ball.reset()
        slep=0.1
    elif ball.xcor() < -360:
        field.increase_left_score()
        left_paddle.reset()
        right_paddle.reset()
        ball.reset()
        slep=0.1
    if(field.right_score>9):
        game_on=False
        field.game_over("Left")
    if(field.left_score>9):
        game_on=False
        field.game_over("Right")
screen.mainloop()
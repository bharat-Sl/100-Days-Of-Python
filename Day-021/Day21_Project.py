#Project Day20
# snake part 2

import turtle
import snake
import food
screen=turtle.Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake=snake.Snake(screen)
snake.play(True)

screen.mainloop()
#challenge 1
import turtle

class mouse:
    def __init__(self):
        self.robot=turtle.Turtle()
    def move_forward(self):
        self.robot.forward(10)
    def move_backward(self):
        self.robot.backward(10)
    def turn_left(self):
        self.robot.left(10)
    def turn_right(self):
        self.robot.right(10)
    def clear(self):
        self.robot.clear()
        self.robot.penup()
        self.robot.home()
        self.robot.pendown()

screen=turtle.Screen()
pen=mouse()
screen.listen()
screen.onkeypress(pen.move_forward,"w")
screen.onkeypress(pen.move_backward,"s")
screen.onkeypress(pen.turn_left,"a")
screen.onkeypress(pen.turn_right,"d")
screen.onkey(pen.clear,"c")
screen.mainloop()
#challenge 1
# robot turn_left() and move() already defined.
# turn_left() spins the robot to left on the spot.
# move() moves the robot one space forward.

# Map:
#5
#4
#3
#2   ⬜️|⬜️⬜️|⬜️⬜️|⬜️⬜️|⬜️⬜️|⬜️⬜️|
#1 S ⬜️|⬜️⬜️|⬜️⬜️|⬜️⬜️|⬜️⬜️|⬜️⬜️|🟥
#  1  2  3  4  5  6  7  8  9 10  11 12 13

#(1,1)is the start and Red box is the goal

#----------------------------------#
def turn_left():
    print("Left")
def move():
    print("Move 1")
def at_goal():
    print('check goal')
#----------------------------------#

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def huddle():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
for i in range(0,6):
    huddle()
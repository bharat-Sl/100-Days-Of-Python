#challenge 4
# robot turn_left(), move(), wall_in_front(), front_is_clear(), wall_on right() and at_goal() already defined.
# turn_left() spins the robot to left on the spot.
# move() moves the robot one space forward.
# at_goal() checks if the robot is at goal and returns true if it reaches the goal.
# wall_in_front() checks if the robot has a wall in front.
# front_is_clear() checks if the robot front is clear.
# wall_on right() checks if the robot has a wall on its right.

# Map:
#5
#4         ⬜️|⬜️
#3         ⬜️|⬜️                 ⬜️|⬜️
#2   ⬜️|⬜️⬜️|⬜️           ⬜️|⬜️⬜️|⬜️
#1 S ⬜️|⬜️⬜️|⬜️⬜️|⬜️⬜️⬜️⬜️|⬜️⬜️|🟥
#  1  2  3  4  5  6  7  8  9 10  11 12 13

#(1,1)is the start and red block is the goal.
#Here walls can be anywhere and can be of any height

#----------------------------------#
def turn_left():
    print("Left")
def move():
    print("Move 1")
def at_goal():
    print('check goal return true if at the goal')
def wall_in_front():
    print('check front return true if there is a wall')
def front_is_clear():
    print('check front return true if front is clear')
def wall_on_right():
    print('check right return true if there is a wall')
#----------------------------------#

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def huddle():
    if(wall_in_front()):
        turn_left()
        while wall_on_right():
            move()
        turn_right()
        move()
        turn_right()
        move()
        while wall_on_right() and front_is_clear():
            move()
        turn_left()
    else:
        move()
while not at_goal():
    huddle()
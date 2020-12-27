#Project Day6

# robot turn_left(), move(), front_is_clear(), right_is_clear() and at_goal() already defined.
# turn_left() spins the robot to left on the spot.
# move() moves the robot one space forward.
# at_goal() checks if the robot is at goal and returns true if it reaches the goal.
# front_is_clear() checks if the robot front is clear.
# right_is_clear() checks if the robot has a wall on its right.

# Map:
#6|______________
#5|         __   |         
#4|__|__      |__🟥
#3|     |      __|
#2|  |  |__|  |  |
#1|__|___________|
#  1  2  3  4  5  

#Start can be anywhere on the map with the robot facing anywhere.
#We have to reach the Red box to win.

#----------------------------------#
def turn_left():
    print("Left")
def move():
    print("Move 1")
def at_goal():
    print('check goal return true if at the goal')
def right_is_clear():
    print('check right return true if right is clear')
def front_is_clear():
    print('check front return true if front is clear')
#----------------------------------#

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while not at_goal():
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()
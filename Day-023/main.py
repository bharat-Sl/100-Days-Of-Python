import time
from turtle import Screen
import crossy
import car
import scoreboard

screen=Screen()
screen.setup(width=600,height=600)
screen.tracer(0)

player=crossy.Crossy(screen)
cars=car.Car()
scoreboard=scoreboard.Scoreboard()

game_on=True 
step=0
limit=0
speed=5
while game_on:
    step+=1
    if(step>=5):
        step=limit
        cars.create_car()
    cars.move_cars(speed)
    for car in cars.all_cars:
        if(car.distance(player)<30 and player.ycor()==car.ycor()):
            game_on=False
            print("end")
            scoreboard.game_over()
            continue
    if(player.ycor()>=250):
            player.reset()
            scoreboard.increase_level()
            speed+=5
            limit+=1
    player.move()
    time.sleep(0.1)
    screen.update()
screen.mainloop()
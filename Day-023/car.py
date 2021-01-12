import random
import turtle

lane=[-190,-170,-150,-130,-110,-90,-70,-50,-30,-10,10,30,50,70,90,110,130,150,170,190]
list_colors=["blue","red","green","purple","orange","yellow","CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
class Car():
    def __init__(self):
        self.all_cars=[]

    def create_car(self):
        new_car=turtle.Turtle("square")
        new_car.shapesize(stretch_wid=1,stretch_len=2)
        new_car.penup()
        new_car.color(random.choice(list_colors))
        new_car.goto(300,random.choice(lane))
        self.all_cars.append(new_car)

    def move_cars(self,speed):
        for car in self.all_cars:
            if(car.xcor()>-320):
                car.back(speed)
            else:
                self.all_cars.remove(car)
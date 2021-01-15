#Project Day25
import os

os.chdir(r"C:\Users\bhara\Desktop\100-Days-of-Python-Projects\Day-025\Day25_Project")
import pandas as pd
import turtle

def getUserInput(screen,number):
    return screen.textinput(
        title=f"{number}/50 States Correct",
        prompt="What's another state name?"
    )

def correctAnswer(screen,x,y,name):
    pen=turtle.Turtle()
    pen.penup()
    pen.hideturtle()
    pen.goto(x,y)
    pen.color("black")
    pen.write(f"{name}")

screen=turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width=730,height=500)
image="blank_states_img.gif"
screen.addshape(image)
robot=turtle.Turtle(image)
data_file=pd.read_csv("50_states.csv")
all_states=data_file.state.to_list()
guessed_states=[]
guess=0
while guess<50:
    new_guess=getUserInput(screen,guess).title()
    if(new_guess=="Exit"):
        break
    if new_guess in all_states:
        if not new_guess in guessed_states:
            x=int(data_file[data_file.state==new_guess].x)
            y=int(data_file[data_file.state==new_guess].y)
            guessed_states.append(new_guess)
            guess+=1
            correctAnswer(screen,x,y,new_guess)

if(guess<50):
    missed_states=list(set(all_states)-set(guessed_states))
    new_data=pd.DataFrame(missed_states)
    new_data.to_csv("states_to_learn.csv")


#Day27 Project
import os
os.chdir(r"C:\Users\bhara\Desktop\100-Days-of-Python-Projects\Day-028")
from tkinter import *
import time
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK="✔"
timer=None
#functional

def startButtonClicked(count=25*60,times=4,txt="Work"):
    minute=math.floor(count/60)
    second=count%60
    if minute<10:
        minute=f"0{minute}"
    if second<10:
        second=f"0{second}"
    global timer
    canvas.itemconfig(timer_text, text=f"{minute}:{second}")
    if count>0:
        label1.config(text=txt)
        timer=window.after(1000,startButtonClicked,count-1,times,txt)
    elif times>1 and txt=="Work":
        checklist[4-times].config(fg=GREEN)
        timer=window.after(1000,startButtonClicked,SHORT_BREAK_MIN*60,times-1,"Rest")
    elif times==1 and txt=="Work":
        checklist[4-times].config(fg=GREEN)
        timer=window.after(1000,startButtonClicked,LONG_BREAK_MIN*60,times-1,"Rest")
    elif times>0:
        timer=window.after(1000,startButtonClicked,WORK_MIN*60,times,"Work")
    
def resetButtonClicked():
    window.after_cancel(timer)
    [check.config(fg=YELLOW) for check in checklist]
    canvas.itemconfig(timer_text, text="00:00")
    label1.config(text="Timer")


window=Tk()
window.title("Pomodoro")
window.config(padx=55,pady=40,bg=YELLOW)

#Labels
label1=Label(text="Timer",bg=YELLOW,fg=GREEN,font=(FONT_NAME,40))
checklist=[Label(text=CHECK,bg=YELLOW,fg=YELLOW,font=(FONT_NAME,18)) for i in range(0,4)]

#buttons
button_start=Button(text="Start",command=startButtonClicked)
button_reset=Button(text="Reset",command=resetButtonClicked)


#Canvas UI
canvas=Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
image=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=image)
timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))

#Displaying UI
label1.grid(row=0,column=1,columnspan=4)
canvas.grid(row=1,column=1,columnspan=4)
button_start.grid(row=2,column=0)
button_reset.grid(row=2,column=5)
checklist[0].grid(row=3,column=1)
checklist[1].grid(row=3,column=2)
checklist[2].grid(row=3,column=3)
checklist[3].grid(row=3,column=4)


window.mainloop()
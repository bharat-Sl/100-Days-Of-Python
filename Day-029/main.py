#Project Day29
import os
os.chdir(r"C:\Users\bhara\Desktop\100-Days-of-Python-Projects\Day-029")
import tkinter as tk
import random
import pyperclip

WHITE="#ffffff"
BLACK="#000000"

# Function to write in the file
def export_file():
    Site=input_box1.get()
    Email=input_box2.get()
    Password=input_box3.get()
    with open("passwords.txt",mode="a") as file:
        if Site!="" or Password!="":
            file.write(f"\n{Site} | {Email} | {Password}") 
            input_box1.delete(0,tk.END)
            input_box2.delete(0,tk.END)
            input_box2.insert(0,"bharatag00@gmail.com")
            input_box3.delete(0,tk.END)
        else:
            print("error")

# Function to generate password
def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    nr_letters = 11
    nr_symbols = 2
    nr_numbers = 3
    total_characters=nr_letters+nr_symbols+nr_numbers
    choosen=[]
    password=''
    for i in range(0,total_characters):
        if(nr_letters>0):
            #chosen.append(random.choice(letters))
            choosen.append(random.choice(letters))  
            nr_letters-=1
        if(nr_numbers>0):
            choosen.append(random.choice(numbers))
            nr_numbers-=1
        if(nr_symbols>0):
            choosen.append(random.choice(symbols))  
            nr_symbols-=1
    for i in range(0,total_characters):
        password+=choosen.pop(random.randint(0,len(choosen)-1))
    pyperclip.copy(password)
    input_box3.delete(0,tk.END)
    input_box3.insert(0,password)




# Setting Up Window
window=tk.Tk()
window.title("Password Manager")
window.config(padx=30,pady=30,bg=WHITE)

#Setting up Elements
#Row 0
canvas=tk.Canvas(width=120,height=160,bg=WHITE,highlightthickness=0)
photo=tk.PhotoImage(file="logo.png")
canvas.create_image(60,80,image=photo)
#Row 1
label1=tk.Label(text="Website:",bg=WHITE,fg=BLACK)
input_box1= tk.Entry(width=40,borderwidth=2,bg=WHITE,highlightcolor="#00afff")
#Row 2
label2=tk.Label(text="Email/Username:",bg=WHITE,fg=BLACK)
input_box2= tk.Entry(width=40,borderwidth=2,bg=WHITE,highlightcolor="#00afff")
input_box2.insert(0,"bharatag00@gmail.com")
#Row 3
label3=tk.Label(text="Password:",bg=WHITE,fg=BLACK)
input_box3= tk.Entry(width=21,borderwidth=2,bg=WHITE,highlightcolor="#00afff")
button1=tk.Button(text="Generate Password",width=15,bg=WHITE,fg=BLACK,command=gen_password)
#Row 4
button2=tk.Button(text="Add",width=34,bg=WHITE,fg=BLACK,command=export_file)


#Putting Elements on screen
canvas.grid(row=0,column=1)
label1.grid(row=1,column=0,sticky="W")
input_box1.grid(row=1,column=1,columnspan=2)
label2.grid(row=2,column=0,sticky="W")
input_box2.grid(row=2,column=1,columnspan=2)
label3.grid(row=3,column=0,sticky="W")
input_box3.grid(row=3,column=1)
button1.grid(row=3,column=2,sticky="W")
button2.grid(row=4,column=1,columnspan=2)




window.mainloop()
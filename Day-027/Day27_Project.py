#Project Day26

# def add(*args,**vargs):
#     sum=0
#     for arg in args:
#         sum+=arg
#     return sum


# print(add(1,2,3,4,5))

import tkinter

def isNumber(s):
 
    for i in range(len(s)):
        if s[i].isdigit() != True:
            return False
    return True

class Workplace:
    def __init__(self):
        self.kilometer=0.0
        self.miles=0
        self.label1=tkinter.Label(window,text="is equal to",font =('Bernard MT', 12))
        self.label2=tkinter.Label(window,text=f"{self.kilometer}",font =('Bernard MT', 12))
        self.label3=tkinter.Label(window,text="Miles",font =('Bernard MT', 12))
        self.label4=tkinter.Label(window,text="Km",font =('Bernard MT', 12))
        self.button=tkinter.Button(text="Calculate", command=self.buttonClicked,font =('Bernard MT', 12))
        self.input_box= tkinter.Entry(width=15)
        self.input_box.grid(column=1,row=0)
        self.label3.grid(column=2,row=0)
        self.label4.grid(column=2,row=1)
        self.label1.grid(column=0,row=1)
        self.label2.grid(column=1,row=1)
        self.button.grid(column=1,row=2)
        
    
    def buttonClicked(self):
        temp=self.input_box.get()
        if isNumber(temp):
            self.kilometer=float(temp)*1.609
        else:
            print("error")
        self.label2.config(text=f"{self.kilometer}")

window=tkinter.Tk()
window.minsize(width=300,height=150)
window.title('Mile to Km Conversion')
window.config(padx=30,pady=30)
window.resizable(0,0)
screen=Workplace()

window.mainloop()

import tkinter
from tkinter import Tk, Label, Entry, StringVar, Button

# Code to add widgets will go here...
master = tkinter.Tk()
'''
def helloCallBack():
    print( "Hello Python", "Hello World")

B = Button(master, text ="Hello", command = helloCallBack)
'''
# add entry box for name
nameText=StringVar()
nameText.set("Please enter your name")
nameLabel=Label(master, textvariable=nameText)
nameLabel.pack()

nameBox = Entry(master)
nameBox.pack()


# add entry box for wakeTime
wakeText=StringVar()
wakeText.set("On average, what time do you wake up?")
wakeLabel=Label(master, textvariable=wakeText, height=4)
wakeLabel.pack()

wakeBox = Entry(master)
wakeBox.pack()

# add entry box for smoke
smokeText=StringVar()
smokeText.set("Are you okay with somking? \n(Y or N): ")
smokeLabel=Label(master, textvariable=smokeText, height=4)
smokeLabel.pack()

SmokeVal = "0"
def assignSmokeYes():
    global SmokeVal
    SmokeVal = "Y"
def assignSmokeNo():
    global SmokeVal
    SmokeVal = "N"
yes_button = Button(master, text ="Yes", command = assignSmokeYes)
yes_button.pack()
no_button = Button(master, text ="No", command = assignSmokeNo)
no_button.pack()

# get all the results

def callback1():
    result = str(nameBox.get())+str(wakeBox.get())+str(SmokeVal)
    print(result)
    
    
b = Button(master, text="Submit", width=10, command = callback1)
b.pack()

master.mainloop()


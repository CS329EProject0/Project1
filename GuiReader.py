
import tkinter
from tkinter import *

# Code to add widgets will go here...
master = tkinter.Tk()

# scroll bar
scrollbar = Scrollbar(master)
scrollbar.pack(side=RIGHT, fill=Y)
listbox = Listbox(master, yscrollcommand=scrollbar.set)
for i in range(1000):
    listbox.insert(END, str(i))
listbox.pack(side=LEFT, fill=BOTH)

scrollbar.config(command=listbox.yview)

# add entry box for name
nameText=StringVar()
nameText.set("Please enter your name")
nameLabel=Label(master, textvariable=nameText)
nameLabel.pack()

nameBox = Entry(master)
nameBox.pack()

# add entry box for sleepTime
sleepText=StringVar()
sleepText.set("On average, what time do you sleep?")
sleepLabel=Label(master, textvariable=sleepText, height=4)
sleepLabel.pack()

sleepBox = Entry(master)
sleepBox.pack()

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

SmokeVal = "0"# check error value
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

# add entry box for gender
genderText=StringVar()
genderText.set("Please choose your gender")
genderLabel=Label(master, textvariable=genderText, height=4)
genderLabel.pack()

genderVal = "0"# check error value
def assignFemale():
    global genderVal
    genderVal = "F"
def assignMale():
    global genderVal
    genderVal = "M"
F_button = Button(master, text ="Female", command = assignFemale)
F_button.pack()
M_button = Button(master, text ="Male", command = assignMale)
M_button.pack()

# add entry box for gender preference
gPreText=StringVar()
gPreText.set("Please choose your preferred roomate gender")
gPreLabel=Label(master, textvariable=smokeText, height=4)
gPreLabel.pack()

gPreVal = "0"
def assigngF():
    global gPreVal
    gPreVal = "F"
def assigngM():
    global gPreVal
    gPreVal = "M"
gF_button = Button(master, text ="Female", command = assigngF)
gF_button.pack()
gM_button = Button(master, text ="Male", command = assigngM)
gM_button.pack()

# add entry box for Cleaness
cleanText=StringVar()
cleanText.set("Please enter your level of cleaniess, from 1-5")
cleanLabel=Label(master, textvariable=cleanText, height=4)
cleanLabel.pack()

cleanBox = Entry(master)
cleanBox.pack()

# add entry box for guests
guestText=StringVar()
guestText.set("Please enter your level acceptance of guests")
guestLabel=Label(master, textvariable=guestText, height=4)
guestLabel.pack()

guestBox = Entry(master)
guestBox.pack()

# add entry box for sound
soundText=StringVar()
soundText.set("On average, what time do you sleep?")
soundLabel=Label(master, textvariable=soundText, height=4)
soundLabel.pack()

soundBox = Entry(master)
soundBox.pack()

# get all the results
def callback1():
    result = str(nameBox.get())+" "+str(sleepBox.get())+" "+str(wakeBox.get())+" "+str(SmokeVal)\
             +" "+str(genderVal)+" "+str(gPreVal)+" "+str(cleanBox.get())+" "+str(guestBox.get())+" "+str(soundBox.get())
    print(result)
    
b = Button(master, text="Submit", width=10, command = callback1)
b.pack()

master.mainloop()


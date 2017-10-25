
import tkinter
from tkinter import *

# Code to add widgets will go here...
master = tkinter.Tk()
# scroll bar, should fix for 3rd release

scrollbar = Scrollbar(master)
scrollbar.pack(side=RIGHT, fill=Y)
listbox = Listbox(master, yscrollcommand=scrollbar.set)

listbox.pack()

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

smokeVal = "0"# check error value
smokeValYes = Radiobutton(master, text ="Yes", variable = smokeVal, value = 'Y')
smokeValYes.pack()
smokeValNo = Radiobutton(master, text ="No", variable = smokeVal, value = 'N')
smokeValNo.pack()

# add entry box for gender
genderText=StringVar()
genderText.set("Please choose your gender")
genderLabel=Label(master, textvariable=genderText, height=4)
genderLabel.pack()

genderVal = ""# check error value

genderValFemale = Radiobutton(master, text ="Female", variable = genderVal, value = 'F')
genderValFemale.pack()
genderValMale = Radiobutton(master, text ="Male", variable = genderVal, value = 'M')
genderValMale.pack()

# add entry box for gender preference
genderPrefText=StringVar()
genderPrefText.set("Please choose your preferred roomate gender")
genderPrefLabel=Label(master, textvariable=genderPrefText, height=4)
genderPrefLabel.pack()

genderPrefVal = ""
genderPrefValFemale = Radiobutton(master, text ="Female", variable = genderPrefVal, value = 'F')
genderPrefValFemale.pack()
genderPrefValMale = Radiobutton(master, text ="Male", variable = genderPrefVal, value = 'M')
genderPrefValMale.pack()

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
             +" " + genderVal + " " + genderPrefVal + " " + (cleanBox.get())+" "+str(guestBox.get())+" "+str(soundBox.get())
    print(result)
    
b = Button(master, text="Submit", width=10, command = callback1)
b.pack()

master.mainloop()


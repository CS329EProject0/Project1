
import tkinter
from tkinter import Tk, Label, Entry, StringVar
'''
# remnant of entry class I should finish
class EntryFormat:
    def __init__(self,labelTxt):
        
        self.label = Label(master, textvariable=labelTxt, height=4)
        self.label.pack(side="left")

        self.nameBox = Entry(master)
        self.nameBox.pack(side="left")
        self.Value = self.nameBox.get()
'''

# Code to add widgets will go here...
master = tkinter.Tk()
# add entry box for name
nameText=StringVar()
nameText.set("Enter directory of log files")
nameLabel=Label(master, textvariable=nameText, height=4)
nameLabel.pack(side="left")

nameBox = Entry(master)
nameBox.pack(side="left")
nameVal = nameBox.get()
# add entry box for sleepTime
sleepText=StringVar()
sleepText.set("On average, what time do you go to sleep? ")
sleepLabel=Label(master, textvariable=sleepText, height=4)
sleepLabel.pack(side="left")

sleepBox = Entry(master)
sleepBox.pack(side="left")
# add entry box for wakeTime
wakeText=StringVar()
wakeText.set("On average, what time do you wake up?")
wakeLabel=Label(master, textvariable=wakeText, height=4)
wakeLabel.pack(side="left")

wakeBox = Entry(master)
wakeBox.pack(side="left")
# add entry box for smoke
smokeText=StringVar()
smokeText.set("Are you okay with somking? \n(Y or N): ")
smokeLabel=Label(master, textvariable=smokeText, height=4)
smokeLabel.pack(side="left")

smokeBox = Entry(master)
smokeBox.pack(side="left")

master.mainloop()



import tkinter
from tkinter import Entry
# Code to add widgets will go here...
master = tkinter.Tk()
# add entry box for name
nameBox = Entry(master)
nameBox.pack()
nameVal = nameBox.get()
# add entry box for sleepTime
sleepBox = Entry(master)
sleepBox.pack()
sleepVal = sleepBox.get()
# add entry box for wakeTime
wakeBox = Entry(master)
wakeBox.pack()
wakeVal = wakeBox.get()
# add entry box for smoke
smokeBox = Entry(master)
smokeBox.pack()
smokeVal = smokeBox.get()
# add entry box for gender
genderBox = Entry(master)
genderBox.pack()
genderVal = genderBox.get()
# add entry box for gPrefer
gPreferBox = Entry(master)
gPreferBox.pack()
gPrefer = gPreferBox.get()
# add entry box for cleaniess
cleanBox = Entry(master)
cleanBox.pack()
cleanVal = cleanBox.get()
# add entry box for guest
GuestBox = Entry(master)
GuestBox.pack()
GuestVal = GuestBox.get()
# add entry box for sound
soundBox = Entry(master)
soundBox.pack()
soundVal = soundBox.get()

master.mainloop()


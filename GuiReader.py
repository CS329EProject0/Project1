import tkinter
from tkinter import *

# scroll bar magic, don't touch
def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox("all"),width=500,height=500)
# begin of GUI loop is here    
master = tkinter.Tk()
# scroll bar magic, don't touch
sizex = 800
sizey = 800
posx  = 100
posy  = 100
master.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))

myframe=Frame(master,relief=GROOVE,width=50,height=100,bd=1)
myframe.place(x=10,y=10)

<<<<<<< HEAD
scrollbar.config(command=listbox.yview)
'''

# add entry boxes for first and last name

firstNameText=StringVar()
firstNameText.set("Please enter your first name:")
firstNameLabel=Label(master, textvariable=firstNameText)
firstNameLabel.pack()

firstNameBox = Entry(master)
firstNameBox.pack()

lastNameText=StringVar()
lastNameText.set("Please enter your last name:")
lastNameLabel=Label(master, textvariable=lastNameText)
lastNameLabel.pack()

lastNameBox = Entry(master)
lastNameBox.pack()
=======
canvas=Canvas(myframe)
frame=Frame(canvas)
myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
canvas.configure(yscrollcommand=myscrollbar.set)

myscrollbar.pack(side="right",fill="y")
canvas.pack(side="left")
canvas.create_window((0,0),window=frame,anchor='nw')
frame.bind("<Configure>",myfunction)

# complete scrollbar magic

# Code to add widgets 
# add entry box for name
'''
nameText=StringVar()
nameText.set("Please enter your name")
nameLabel=Label(master, textvariable=nameText)
nameLabel.pack()

'''
Label(frame,text="Please enter your name").grid(row=1,column=0)
Label(frame,text="On average, what time do you sleep?").grid(row=2,column=0)
'''

nameBox = Entry(master)
nameBox.pack()
>>>>>>> c5a7278b5575ff5991507537202d0aa9503ab278

# add entry box for sleepTime
sleepText=StringVar()
sleepText.set("On average, what time do you go to sleep?")
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

# add entry box for gender
genderText=StringVar("")
genderText.set("Please select your gender:")
genderLabel=Label(master, textvariable=genderText, height=4)
genderLabel.pack()


genderVal = StringVar()
genderVal.set("N/A")

genderValFemale = Radiobutton(master, text ="Female", variable = genderVal, value = 'F')
genderValFemale.pack()
genderValMale = Radiobutton(master, text ="Male", variable = genderVal, value = 'M')
genderValMale.pack()

# add entry box for gender preference
genderPrefText=StringVar()
genderPrefText.set("Please select your preferred roomate gender:")
genderPrefLabel=Label(master, textvariable=genderPrefText, height=4)
genderPrefLabel.pack()

genderPrefVal = StringVar()
genderPrefVal.set("N/A")
genderPrefValFemale = Radiobutton(master, text ="Female", variable = genderPrefVal, value = 'F')
genderPrefValFemale.pack()
genderPrefValMale = Radiobutton(master, text ="Male", variable = genderPrefVal, value = 'M')
genderPrefValMale.pack()

# add entry box for smoke
smokeText=StringVar()
smokeText.set("Are you okay with somking? \n(Y or N):")
smokeLabel=Label(master, textvariable=smokeText, height=4)
smokeLabel.pack()

smokeVal = StringVar()
smokeVal.set("N/A")
smokeValYes = Radiobutton(master, text ="Yes", variable = smokeVal, value = 'Y')
smokeValYes.pack()
smokeValNo = Radiobutton(master, text ="No", variable = smokeVal, value = 'N')
smokeValNo.pack()

# add entry box for Cleaness
cleanText=StringVar()
cleanText.set("Please enter your level of cleaniess, from 1-5")
cleanLabel=Label(master, textvariable=cleanText, height=4)
cleanLabel.pack()

cleanBox = Entry(master)
cleanBox.pack()

# add entry box for guests
guestText=StringVar()
guestText.set("Please enter your comfortability with guests")
guestLabel=Label(master, textvariable=guestText, height=4)
guestLabel.pack()

guestBox = Entry(master)
guestBox.pack()

# add entry box for sound
soundText=StringVar()
soundText.set("How comfortable are you with noise?")
soundLabel=Label(master, textvariable=soundText, height=4)
soundLabel.pack()

soundBox = Entry(master)
soundBox.pack()

# get all the results
def callback1():
    result = str(firstNameBox.get())+" "+lastNameBox.get()+" "+str(sleepBox.get())+" "+str(wakeBox.get())+" "+str(SmokeVal)\
             +" " + genderVal + " " + genderPrefVal + " " + (cleanBox.get())+" "+str(guestBox.get())+" "+str(soundBox.get())
    print(result)
    
b = Button(master, text="Submit", width=10, command = callback1)
b.pack()
<<<<<<< HEAD

master.mainloop()
=======
'''
master.mainloop()
>>>>>>> c5a7278b5575ff5991507537202d0aa9503ab278


import tkinter
from tkinter import *

# scroll bar magic, don't touch
def myfunction(event):
    canvas.configure(scrollregion=canvas.bbox("all"),width=500,height=500)
# begin of GUI loop is here    
master = tkinter.Tk()
<<<<<<< HEAD
<<<<<<< HEAD
# scroll bar, should fix for 3rd release

scrollbar = Scrollbar(master)
scrollbar.pack(side=RIGHT, fill=Y)
listbox = Listbox(master, yscrollcommand=scrollbar.set)
=======
=======
>>>>>>> 4ed806bb1142168092d6c518d61bc8372c975f8f
# scroll bar magic, don't touch
sizex = 800
sizey = 800
posx  = 100
posy  = 100
master.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))
<<<<<<< HEAD
>>>>>>> 4ed806bb1142168092d6c518d61bc8372c975f8f

myframe=Frame(master,relief=GROOVE,width=50,height=100,bd=1)
myframe.place(x=10,y=10)

<<<<<<< HEAD
scrollbar.config(command=listbox.yview)

=======
canvas=Canvas(myframe)
frame=Frame(canvas)
myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
canvas.configure(yscrollcommand=myscrollbar.set)

=======

myframe=Frame(master,relief=GROOVE,width=50,height=100,bd=1)
myframe.place(x=10,y=10)

canvas=Canvas(myframe)
frame=Frame(canvas)
myscrollbar=Scrollbar(myframe,orient="vertical",command=canvas.yview)
canvas.configure(yscrollcommand=myscrollbar.set)

>>>>>>> 4ed806bb1142168092d6c518d61bc8372c975f8f
myscrollbar.pack(side="right",fill="y")
canvas.pack(side="left")
canvas.create_window((0,0),window=frame,anchor='nw')
frame.bind("<Configure>",myfunction)

# complete scrollbar magic

# Code to add widgets 
<<<<<<< HEAD
>>>>>>> 4ed806bb1142168092d6c518d61bc8372c975f8f
=======
>>>>>>> 4ed806bb1142168092d6c518d61bc8372c975f8f
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
'''
master.mainloop()


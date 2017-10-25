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

Label(frame,text="Please enter your name").grid(row=1,column=0)
nameBox = Entry(frame)
nameBox.grid(row=2,column=0)

# add entry box for sleepTime
Label(frame,text="On average, what time do you sleep?").grid(row=3,column=0)
sleepBox = Entry(frame)
sleepBox.grid(row=4,column=0)

# add entry box for wakeTime
Label(frame,text="On average, what time do you wake up?").grid(row=5,column=0)
wakeBox = Entry(frame)
wakeBox.grid(row=6,column=0)

# add entry box for gender
Label(frame,text="Please select your gender:").grid(row=7,column=0)

genderVal = StringVar()
genderVal.set("N/A")

genderValFemale = Radiobutton(frame, text ="Female", variable = genderVal, value = 'F')
genderValFemale.grid(row=8,column=0)
genderValMale = Radiobutton(frame, text ="Male", variable = genderVal, value = 'M')
genderValMale.grid(row=9,column=0)

# add entry box for gender preference
Label(frame,text="Please select your preferred roomate gender:").grid(row=10,column=0)

genderPrefVal = StringVar()
genderPrefVal.set("N/A")

genderPrefValFemale = Radiobutton(frame, text ="Female", variable = genderPrefVal, value = 'F')
genderPrefValFemale.grid(row=11,column=0)
genderPrefValMale = Radiobutton(frame, text ="Male", variable = genderPrefVal, value = 'M')
genderPrefValMale.grid(row=12,column=0)

# add entry box for smoke
Label(frame,text="Are you okay with somking? \n(Y or N):").grid(row=13,column=0)

smokeVal = StringVar()
smokeVal.set("N/A")

smokeValYes = Radiobutton(frame, text ="Yes", variable = smokeVal, value = 'Y')
smokeValYes.grid(row=14,column=0)
smokeValNo = Radiobutton(frame, text ="No", variable = smokeVal, value = 'N')
smokeValNo.grid(row=15,column=0)

# add entry box for Cleaness
Label(frame,text="Please enter your level of cleaniess, from 1-5").grid(row=16,column=0)
cleanBox = Entry(frame)
cleanBox.grid(row=17,column=0)

# add entry box for guests
Label(frame,text="Please enter your comfortability with guests").grid(row=18,column=0)
guestBox = Entry(frame)
guestBox.grid(row=19,column=0)

# add entry box for sound
Label(frame,text="Please enter your level of comfortability with sound").grid(row=20,column=0)
soundBox = Entry(frame)
soundBox.grid(row=21,column=0)

# get all the results
def callback1():
    result = str(nameBox.get())+" "+str(sleepBox.get())+" "+str(wakeBox.get())\
             +" " + str(genderVal.get()) + " " + str(genderPrefVal.get()) + " "+str(smokeVal.get())+" " + str(cleanBox.get())+" "+str(guestBox.get())+" "+str(soundBox.get())
    print(result)
    
b = Button(frame, text="Submit", width=10, command = callback1)
b.grid(row=22,column=0)

master.mainloop()




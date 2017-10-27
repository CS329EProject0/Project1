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
# add entry box for first name
Label(frame,text="Please enter your first name").grid(row=1,column=0)
firstNameBox = Entry(frame)
firstNameBox.grid(row=2,column=0)

# add entry box for last name
Label(frame,text="Please enter your last name").grid(row=3,column=0)
lastNameBox = Entry(frame)
lastNameBox.grid(row=4,column=0)

# add entry box for Cleaness
Label(frame,text="On a scale of 1 to 5, how clean are you? \n(1= not clean, 5 = very clean): ").grid(row=5,column=0)
cleanBox = Entry(frame)
cleanBox.grid(row=6,column=0)

# add entry box for guests
Label(frame,text="On a scale of 1 to 5, how comfortable are you with guests in the room? \n(1 = not comfortable, 5 = very comfortable): ").grid(row=7,column=0)
guestBox = Entry(frame)
guestBox.grid(row=8,column=0)

# add entry box for sound
Label(frame,text="On a scale of 1 to 5, how comfortable with noise are you?\n(1 = not comfortable, 5 = very comfortable): ").grid(row=9,column=0)
soundBox = Entry(frame)
soundBox.grid(row=10,column=0)

# add entry box for smoke
Label(frame,text="Are you okay with somking? \n(Y or N):").grid(row=11,column=0)

smokeVal = StringVar()
smokeVal.set("N/A")

smokeValYes = Radiobutton(frame, text ="Yes", variable = smokeVal, value = 'Y')
smokeValYes.grid(row=12,column=0)
smokeValNo = Radiobutton(frame, text ="No", variable = smokeVal, value = 'N')
smokeValNo.grid(row=13,column=0)

# add entry box for drinking
Label(frame,text="Are you okay with drinking? \n(Y or N):").grid(row=14,column=0)

drinkVal = StringVar()
drinkVal.set("N/A")

drinkValYes = Radiobutton(frame, text ="Yes", variable = drinkVal, value = 'Y')
drinkValYes.grid(row=15,column=0)
drinkValNo = Radiobutton(frame, text ="No", variable = drinkVal, value = 'N')
drinkValNo.grid(row=16,column=0)

# add entry box for study habits
Label(frame,text="Do you study at home? \n(Y or N):").grid(row=17,column=0)

studyLocVal = StringVar()
studyLocVal.set("N/A")

studyLocValYes = Radiobutton(frame, text ="Yes", variable = studyLocVal, value = 'Y')
studyLocValYes.grid(row=18,column=0)
studyLocValNo = Radiobutton(frame, text ="No", variable = studyLocVal, value = 'N')
studyLocValNo.grid(row=19,column=0)

# add entry box for gender
Label(frame,text="Do you identify as  male or female or N/A? \n(M, F): ").grid(row=20,column=0)

genderVal = StringVar()
genderVal.set("N/A")

genderValFemale = Radiobutton(frame, text ="Female", variable = genderVal, value = 'F')
genderValFemale.grid(row=21,column=0)
genderValMale = Radiobutton(frame, text ="Male", variable = genderVal, value = 'M')
genderValMale.grid(row=22,column=0)

# add entry box for gender preference
Label(frame,text="Do you prefer to room with a male or female? \n(M, F): ").grid(row=23,column=0)

genderPrefVal = StringVar()
genderPrefVal.set("N/A")

genderPrefValFemale = Radiobutton(frame, text ="Female", variable = genderPrefVal, value = 'F')
genderPrefValFemale.grid(row=24,column=0)
genderPrefValMale = Radiobutton(frame, text ="Male", variable = genderPrefVal, value = 'M')
genderPrefValMale.grid(row=25,column=0)

# add entry box for studyHours
Label(frame,text="\nOn average, how many hours do you study a week \n(1 = 0-2 hrs, 2 = 3-6 hrs, 3 = 7+ hrs): ").grid(row=26,column=0)

studyHrsBox = Entry(frame)
studyHrsBox.grid(row=27,column=0)

# ass entry box for tvHours
Label(frame,text="\nOn average, how many hours do you watch tv a week \n(1 = 0-2 hrs, 2 = 3-6 hrs, 3 = 7+ hrs): ").grid(row=28,column=0)

tvHrsBox = Entry(frame)
tvHrsBox.grid(row=29,column=0)

# add entry box for allNighters
Label(frame,text="\nHow often do you pull all nighters \n(1 = Never, 2 = Sometimes, 3 = Often): ").grid(row=30,column=0)

allNightBox = Entry(frame)
allNightBox.grid(row=31,column=0)

# add entry box for sleepTime
Label(frame,text="\nOn average, what time do you go to sleep? \n(1 = before 10pm, 2 = 10pm-12am, 3 = after 12am): ").grid(row=32,column=0)
sleepBox = Entry(frame)
sleepBox.grid(row=33,column=0)

# add entry box for wakeTime
Label(frame,text="\nOn average, what time do you wake up? \n(1 = before 7am, 2 = 7am-9am, 3 = after 9am: ").grid(row=34,column=0)
wakeBox = Entry(frame)
wakeBox.grid(row=35,column=0)

# get all the results
def callback1():
    result = str(firstNameBox.get())+" "+str(lastNameBox.get())+" " + str(cleanBox.get())+" "+str(guestBox.get())+" "\
             +str(soundBox.get())+ " "+str(smokeVal.get())+" "+str(drinkVal.get())+" "+str(studyLocVal.get())+" "\
             + str(genderVal.get()) + " " + str(genderPrefVal.get())+" "+str(studyHrsBox.get())+" "+str(tvHrsBox.get())+" "\
             +str(allNightBox.get())+" "+str(sleepBox.get())+" "+str(wakeBox.get())
    print(result)



b = Button(frame, text="Submit", width=10, command = callback1)
b.grid(row=36,column=0)


master.mainloop()




import tkinter
from tkinter import *

# scroll bar magic, don't touch
class GUI():
	def __init__(self, master):
		self.master = master

		self.master.title('Please answer the following questions.')

		# scroll bar magic, don't touch
		sizex = 540
		sizey = 500
		posx  = 100
		posy  = 100
		self.master.wm_geometry("%dx%d+%d+%d" % (sizex, sizey, posx, posy))

		myframe=Frame(self.master,relief=GROOVE,width=50,height=100,bd=1)
		myframe.place(x=10,y=10)

		self.canvas=Canvas(myframe)
		frame=Frame(self.canvas)
		myscrollbar=Scrollbar(myframe,orient="vertical",command=self.canvas.yview)
		self.canvas.configure(yscrollcommand=myscrollbar.set)

		myscrollbar.pack(side="right",fill="y")
		self.canvas.pack(side="left")
		self.canvas.create_window((0,0),window=frame,anchor='nw')
		frame.bind("<Configure>", self.myfunction)

		# complete scrollbar magic

		# Code to add widgets 
		# add entry box for first name
		Label(frame,text="Please enter your first name").grid(row=1,column=0)
		self.firstNameBox = Entry(frame)
		self.firstNameBox.grid(row=2,column=0)

		# add entry box for last name
		Label(frame,text="Please enter your last name").grid(row=3,column=0)
		self.lastNameBox = Entry(frame)
		self.lastNameBox.grid(row=4,column=0)

		# add entry box for Cleaness
		Label(frame,text="On a scale of 1 to 5, how clean are you? \n(1= not clean, 5 = very clean): ").grid(row=5,column=0)
		self.cleanBox = Entry(frame)
		self.cleanBox.grid(row=6,column=0)

		# add entry box for guests
		Label(frame,text="On a scale of 1 to 5, how comfortable are you with guests in the room? \n(1 = not comfortable, 5 = very comfortable): ").grid(row=7,column=0)
		self.guestBox = Entry(frame)
		self.guestBox.grid(row=8,column=0)

		# add entry box for sound
		Label(frame,text="On a scale of 1 to 5, how comfortable with noise are you?\n(1 = not comfortable, 5 = very comfortable): ").grid(row=9,column=0)
		self.soundBox = Entry(frame)
		self.soundBox.grid(row=10,column=0)

		# add entry box for smoke
		Label(frame,text="Are you okay with somking? \n(Y or N):").grid(row=11,column=0)

		self.smokeVal = StringVar()
		self.smokeVal.set("N/A")

		self.smokeValYes = Radiobutton(frame, text ="Yes", variable = self.smokeVal, value = 'Y')
		self.smokeValYes.grid(row=12,column=0)
		self.smokeValNo = Radiobutton(frame, text ="No", variable = self.smokeVal, value = 'N')
		self.smokeValNo.grid(row=13,column=0)

		# add entry box for drinking
		Label(frame,text="Are you okay with drinking? \n(Y or N):").grid(row=14,column=0)

		self.drinkVal = StringVar()
		self.drinkVal.set("N/A")

		self.drinkValYes = Radiobutton(frame, text ="Yes", variable = self.drinkVal, value = 'Y')
		self.drinkValYes.grid(row=15,column=0)
		self.drinkValNo = Radiobutton(frame, text ="No", variable = self.drinkVal, value = 'N')
		self.drinkValNo.grid(row=16,column=0)

		# add entry box for study habits
		Label(frame,text="Do you study at home? \n(Y or N):").grid(row=17,column=0)

		self.studyLocVal = StringVar()
		self.studyLocVal.set("N/A")

		self.studyLocValYes = Radiobutton(frame, text ="Yes", variable = self.studyLocVal, value = 'Y')
		self.studyLocValYes.grid(row=18,column=0)
		self.studyLocValNo = Radiobutton(frame, text ="No", variable = self.studyLocVal, value = 'N')
		self.studyLocValNo.grid(row=19,column=0)

		# add entry box for gender
		Label(frame,text="Do you identify as  male or female or N/A? \n(M, F): ").grid(row=20,column=0)

		self.genderVal = StringVar()
		self.genderVal.set("N/A")

		self.genderValFemale = Radiobutton(frame, text ="Female", variable = self.genderVal, value = 'F')
		self.genderValFemale.grid(row=21,column=0)
		self.genderValMale = Radiobutton(frame, text ="Male", variable = self.genderVal, value = 'M')
		self.genderValMale.grid(row=22,column=0)

		# add entry box for gender preference
		Label(frame,text="Do you prefer to room with a male or female? \n(M, F): ").grid(row=23,column=0)

		self.genderPrefVal = StringVar()
		self.genderPrefVal.set("N/A")

		self.genderPrefValFemale = Radiobutton(frame, text ="Female", variable = self.genderPrefVal, value = 'F')
		self.genderPrefValFemale.grid(row=24,column=0)
		self.genderPrefValMale = Radiobutton(frame, text ="Male", variable = self.genderPrefVal, value = 'M')
		self.genderPrefValMale.grid(row=25,column=0)

		# add entry box for studyHours
		Label(frame,text="\nOn average, how many hours do you study a week \n(1 = 0-2 hrs, 2 = 3-6 hrs, 3 = 7+ hrs): ").grid(row=26,column=0)

		self.studyHrsBox = Entry(frame)
		self.studyHrsBox.grid(row=27,column=0)

		# ass entry box for tvHours
		Label(frame,text="\nOn average, how many hours do you watch tv a week \n(1 = 0-2 hrs, 2 = 3-6 hrs, 3 = 7+ hrs): ").grid(row=28,column=0)

		self.tvHrsBox = Entry(frame)
		self.tvHrsBox.grid(row=29,column=0)

		# add entry box for allNighters
		Label(frame,text="\nHow often do you pull all nighters \n(1 = Never, 2 = Sometimes, 3 = Often): ").grid(row=30,column=0)

		self.allNightBox = Entry(frame)
		self.allNightBox.grid(row=31,column=0)

		# add entry box for sleepTime
		Label(frame,text="\nOn average, what time do you go to sleep? \n(1 = before 10pm, 2 = 10pm-12am, 3 = after 12am): ").grid(row=32,column=0)
		self.sleepBox = Entry(frame)
		self.sleepBox.grid(row=33,column=0)

		# add entry box for wakeTime
		Label(frame,text="\nOn average, what time do you wake up? \n(1 = before 7am, 2 = 7am-9am, 3 = after 9am: ").grid(row=34,column=0)
		self.wakeBox = Entry(frame)
		self.wakeBox.grid(row=35,column=0)


		b = Button(frame, text="Submit", width=10, command = self.callback1)
		b.grid(row=36,column=0)


	# append the results to the people database and kill the GUI
	def callback1(self):
		'''
		result = str(self.firstNameBox.get())+" "+str(self.lastNameBox.get())+" " + str(self.cleanBox.get())+" "+str(self.guestBox.get())+" "\
				 +str(self.soundBox.get())+ " "+str(self.smokeVal.get())+" "+str(self.drinkVal.get())+" "+str(self.studyLocVal.get())+" "\
		 		 + str(self.genderVal.get()) + " " + str(self.genderPrefVal.get())+" "+str(self.studyHrsBox.get())+" "+str(self.tvHrsBox.get())+" "\
		 		 +str(self.allNightBox.get())+" "+str(self.sleepBox.get())+" "+str(self.wakeBox.get())

		 '''

		result = str(self.firstNameBox.get())

		infile = open("Roommates.txt","a")
		infile.write(result)
		infile.close()

		self.master.quit()


	def myfunction(self, event):
		self.canvas.configure(scrollregion=self.canvas.bbox("all"),width=500,height=500)

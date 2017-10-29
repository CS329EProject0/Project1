import tkinter
from tkinter import *
from tkinter import messagebox

# scroll bar magic, don't touch
class GUI():
	def __init__(self, master):
		self.master = master

		self.master.title('The Roommate Guru')

		# add backgroud color
		master.configure(bg='antique white')

		# scroll bar magic, don't touch
		sizex = 440
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

		# color design for GUI
		backgroundColor = "floral white"
		textColor = "#662E1C"
		# add frame color
		self.canvas.configure(bg='floral white')
		frame.configure(bg='floral white')

		
		# Code to add widgets 
		# add entry box for first and last names
		Label(frame,fg = textColor,bg = backgroundColor,text="Please enter your first name:").grid(row=1,column=0)

		self.firstNameBox = Entry(frame)
		self.firstNameBox.grid(row=2,column=0)

		# add entry box for last name
		Label(frame,fg = textColor,bg = backgroundColor, text="Please enter your last name:").grid(row=3,column=0)

		self.lastNameBox = Entry(frame)
		self.lastNameBox.grid(row=4,column=0)


		# START: qualitative textbox entry questions
		# add entry box for Cleaness
		Label(frame,fg = textColor,bg = backgroundColor, text="On a scale of 1 to 5, how clean are you? \n(1= I can't see the floor.  5 = OCD) ").grid(row=5,column=0)

		self.cleanBox = Entry(frame)
		self.cleanBox.grid(row=6,column=0)

		# add entry box for guests
		Label(frame,fg = textColor,bg = backgroundColor, text="On a scale of 1 to 5, how comfortable are you with guests in the room? \n(1 = People? No thanks.  5 = Partayy!) ").grid(row=7,column=0)
		self.guestBox = Entry(frame)
		self.guestBox.grid(row=8,column=0)

		# add entry box for sound
		Label(frame,fg = textColor, bg = backgroundColor, text="On a scale of 1 to 5, how comfortable with noise are you?\n(1 = It's better if we just don't talk.  5 = I'm pretty much in a band.").grid(row=9,column=0)

		self.soundBox = Entry(frame)
		self.soundBox.grid(row=10,column=0)


		# START: radiobutton questions
		# add entry box for smoke
		Label(frame,fg = textColor, bg = backgroundColor, text="Are you okay with smoking?").grid(row=11,column=0)


		self.smokeVal = StringVar()
		self.smokeVal.set("N/A")

		self.smokeValYes = Radiobutton(frame, fg = textColor, bg = backgroundColor, text ="Yes", variable = self.smokeVal, value = 'Y')
		self.smokeValYes.grid(row=12,column=0)
		self.smokeValNo = Radiobutton(frame, fg = textColor, bg = backgroundColor, text ="No", variable = self.smokeVal, value = 'N')
		self.smokeValNo.grid(row=13,column=0)

		# add entry box for drinking
		Label(frame,fg = textColor, bg = backgroundColor, text="Are you okay with drinking?").grid(row=14,column=0)


		self.drinkVal = StringVar()
		self.drinkVal.set("N/A")

		self.drinkValYes = Radiobutton(frame, fg = textColor, bg = backgroundColor, text ="Yes", variable = self.drinkVal, value = 'Y')
		self.drinkValYes.grid(row=15,column=0)
		self.drinkValNo = Radiobutton(frame, fg = textColor, bg = backgroundColor, text ="No", variable = self.drinkVal, value = 'N')
		self.drinkValNo.grid(row=16,column=0)

		# add entry box for study habits
		Label(frame,fg = textColor, bg = backgroundColor, text="Do you study at home?").grid(row=17,column=0)


		self.studyLocVal = StringVar()
		self.studyLocVal.set("N/A")

		self.studyLocValYes = Radiobutton(frame, fg = textColor, bg = backgroundColor, text ="Yes", variable = self.studyLocVal, value = 'Y')
		self.studyLocValYes.grid(row=18,column=0)
		self.studyLocValNo = Radiobutton(frame, fg = textColor, bg = backgroundColor, text ="No", variable = self.studyLocVal, value = 'N')
		self.studyLocValNo.grid(row=19,column=0)

		# add entry box for gender
		Label(frame,fg = textColor, bg = backgroundColor, text="Do you identify as  male or female?").grid(row=20,column=0)

		self.genderVal = StringVar()
		self.genderVal.set("N/A")

		self.genderValFemale = Radiobutton(frame, fg = textColor, bg = backgroundColor, text ="Female", variable = self.genderVal, value = 'F')
		self.genderValFemale.grid(row=21,column=0)
		self.genderValMale = Radiobutton(frame, fg = textColor, bg = backgroundColor, text ="Male", variable = self.genderVal, value = 'M')
		self.genderValMale.grid(row=22,column=0)

		# add entry box for gender preference
		Label(frame,fg = textColor, bg = backgroundColor, text="Do you prefer to room with a male or female?").grid(row=23,column=0)

		self.genderPrefVal = StringVar()
		self.genderPrefVal.set("N/A")

		self.genderPrefValFemale = Radiobutton(frame, fg = textColor, bg = backgroundColor, text ="Female", variable = self.genderPrefVal, value = 'F')
		self.genderPrefValFemale.grid(row=24,column=0)
		self.genderPrefValMale = Radiobutton(frame, fg = textColor, bg = backgroundColor, text ="Male", variable = self.genderPrefVal, value = 'M')
		self.genderPrefValMale.grid(row=25,column=0)


		# START: quantitative textbox questions

		# add entry box for studyHours
		Label(frame,fg = textColor,bg = backgroundColor,text="On average, how many hours do you study a week \n(1 = 0-2 hrs, 2 = 3-6 hrs, 3 = 7+ hrs): ").grid(row=26,column=0)

		self.studyHrsBox = Entry(frame)
		self.studyHrsBox.grid(row=27,column=0)

		# ass entry box for tvHours
		Label(frame,fg = textColor,bg = backgroundColor,text="On average, how many hours do you watch tv a week \n(1 = 0-2 hrs, 2 = 3-6 hrs, 3 = 7+ hrs): ").grid(row=28,column=0)

		self.tvHrsBox = Entry(frame)
		self.tvHrsBox.grid(row=29,column=0)

		# add entry box for allNighters
		Label(frame,fg = textColor,bg = backgroundColor,text="How often do you pull all nighters \n(1 = Never, 2 = Sometimes, 3 = Often): ").grid(row=30,column=0)

		self.allNightBox = Entry(frame)
		self.allNightBox.grid(row=31,column=0)

		# add entry box for sleepTime
		Label(frame,fg = textColor,bg = backgroundColor,text="On average, what time do you go to sleep? \n(1 = before 10pm, 2 = 10pm-12am, 3 = after 12am): ").grid(row=32,column=0)
		self.sleepBox = Entry(frame)
		self.sleepBox.grid(row=33,column=0)

		# add entry box for wakeTime
		Label(frame,fg = textColor,bg = backgroundColor,text="On average, what time do you wake up? \n(1 = before 7am, 2 = 7am-9am, 3 = after 9am: ").grid(row=34,column=0)
		self.wakeBox = Entry(frame)
		self.wakeBox.grid(row=35,column=0)


		b = Button(frame, bg = "misty rose",text="Submit", width=10, command = self.callback)
		b.grid(row=36,column=0, pady = 20)


	def callback(self):

		# create a list of each piece of data for easier error checking,
		# also so that the data is organized according to the format read by sortRoommates.py
		dataList = [self.firstNameBox.get(), self.lastNameBox.get(), self.sleepBox.get(), self.wakeBox.get(), self.smokeVal.get(), self.drinkVal.get(),   \
		self.studyLocVal.get(), self.studyHrsBox.get(), self.tvHrsBox.get(), self.allNightBox.get(), self.genderVal.get(), self.genderPrefVal.get(), self.cleanBox.get(), self.soundBox.get(), \
		self.guestBox.get()]

		# the following lists are for error checking when creating the unique error statement below
		nameIndicies = [0, 1]
		relativeRangeIndicies = [2, 3, 7, 8, 9]
		discreteIndicies = [12, 13, 14]

		# initialize 3 different error variables
		spaceInBox = False
		emptyBox = False
		unselectedRadioButton = False
		nameError = False
		numNotInRangeError = False
		textBoxNumericError = False

		# ensure each piece of data conforms to appropriate format
		for idx in range (len(dataList)):	
			# check if a text box is empty		
			if dataList[idx] == '':
				emptyBox = True
				break

			# check if there is a space in a text box
			if ' ' in dataList[idx]:
				spaceInBox = True
				break

			# check if one of the radiobutton questions returned an invalid response
			if dataList[idx] == "N/A":
				unselectedRadioButton = True
				break

			# check that the name entry boxes contain only letters
			if idx in nameIndicies:
				if not dataList[idx].isalpha():
					nameError = True
					break

			# check that the text entry boxes are numeric and within the specified range
			if idx in discreteIndicies:
				val = (dataList[idx])
				if val.isnumeric():
					val = int(val)
					if val > 0 and val < 6:
						continue
					else:
						numNotInRangeError = True
						break
				else:
					textBoxNumericError = True
					break
			if idx in relativeRangeIndicies:
				val = (dataList[idx])
				if val.isnumeric():
					val = int(val)
					if val > 0 and val < 4:
						continue
					else:
						numNotInRangeError = True
						break
				else:
					textBoxNumericError = True
					break


		# initialize the error string
		errorString = ""
		errorTitle = "One or more of your inputs is invalid."

		# check if any of the errors occured, and customize and return the error message
		if spaceInBox or emptyBox or unselectedRadioButton or nameError or textBoxNumericError or numNotInRangeError:
			if spaceInBox:
				errorString += "Make sure there aren't any spaces in the text fields."

			if emptyBox:
				errorString += "Make sure you've filled in each input field."

			if unselectedRadioButton:
				errorString += "Double check that a button is selected in each field."

			if nameError:
				errorString += "Only enter letters into the name entry boxes."

			if textBoxNumericError:
				errorString += "Ensure that you only entered integers in the text boxes."

			if numNotInRangeError:
				errorString += "Be sure to only enter integers within the specified range."

			# figure out how to display popups, for now just print the error
			# message.showerror("Error", errorString)
			messagebox.showerror(errorTitle, errorString)

		# if no errors occurred, add the user to the database and kill the program
		else:
			result = ''
			for data in dataList:
				result += data + ' '
			result = result[:-1]

			infile = open("newUserTemp.txt","w")
			infile.write(result)
			infile.close()

			self.master.destroy()

	# configures scrollbar
	def myfunction(self, event):
		self.canvas.configure(scrollregion=self.canvas.bbox("all"),width=400,height=500)
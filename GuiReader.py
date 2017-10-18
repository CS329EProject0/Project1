
import tkinter
from tkinter import Tk, Label, Entry, StringVar, Button
'''
class EntryFormat:
    def __init__(self,master):
        
        self.resultAns = ""
        self.master = master
        master.title("user survey")
        
        # enter the name
        self.label = Label(master, text="Please enter your name: ")
        self.label.pack()

        self.nameBox = Entry(master)
        self.nameBox.pack()
        self.resultAns += str(self.nameBox.get())
        # enter the sleep time



'''
# Code to add widgets will go here...
master = tkinter.Tk()

# add entry box for name
nameText=StringVar()
nameText.set("Please enter your name")
nameLabel=Label(master, textvariable=nameText)
nameLabel.pack()

nameBox = Entry(master)
nameBox.pack()


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

smokeBox = Entry(master)
smokeBox.pack()

# get all the results
def callback1():
    print(nameBox.get())
    print(wakeBox.get())
    print(smokeBox.get())
    
b = Button(master, text="get", width=10, command=callback1)
b.pack()


master.mainloop()


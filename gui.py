from tkinter import Tk, Label, Button

class MyFirstGUI:
    def __init__(self, master):
        self.master = master
        master.title("A simple GUI")

        self.label = Label(master, text="On a scale of 1 to 5, how clean are you? \n(1= not clean, 5 = very clean): ")
        self.label.pack()

        self.one_button = Button(master, text="1", command=self.assign1)
        self.one_button.pack()
        self.two_button = Button(master, text="2", command=self.assign2)
        self.two_button.pack()
        self.three_button = Button(master, text="3", command=self.assign3)
        self.three_button.pack()
        self.four_button = Button(master, text="4", command=self.assign4)
        self.four_button.pack()
        self.five_button = Button(master, text="5", command=self.assign5)
        self.five_button.pack()

        self.label = Label(master, text="On a scale of 1 to 5, how comfortable are you with guests in the room? \n(1 = not comfortable, 5 = very comfortable): ")
        self.label.pack()

        self.one_button = Button(master, text="1", command=self.assign1)
        self.one_button.pack()
        self.two_button = Button(master, text="2", command=self.assign2)
        self.two_button.pack()
        self.three_button = Button(master, text="3", command=self.assign3)
        self.three_button.pack()
        self.four_button = Button(master, text="4", command=self.assign4)
        self.four_button.pack()
        self.five_button = Button(master, text="5", command=self.assign5)
        self.five_button.pack()

        self.label = Label(master, text="On a scale of 1 to 5, how comfortable with noise are you?\n(1 = not comfortable, 5 = very comfortable):")
        self.label.pack()

        self.one_button = Button(master, text="1", command=self.assign1)
        self.one_button.pack()
        self.two_button = Button(master, text="2", command=self.assign2)
        self.two_button.pack()
        self.three_button = Button(master, text="3", command=self.assign3)
        self.three_button.pack()
        self.four_button = Button(master, text="4", command=self.assign4)
        self.four_button.pack()
        self.five_button = Button(master, text="5", command=self.assign5)
        self.five_button.pack()

        self.label = Label(master, text="Are you okay with smoking? \n(Y or N):")
        self.label.pack()

        self.y_button = Button(master, text='Yes', command=self.assignY)
        self.y_button.pack()
        self.y_button = Button(master, text='No', command=self.assignN)
        self.y_button.pack()

        self.label = Label(master, text="Do you identify as male or female?")
        self.label.pack()

        self.male_button = Button(master, text="Male", command=self.assignMale)
        self.male_button.pack()
        self.female_button = Button(master, text="Female", command=self.assignFemale)
        self.female_button.pack()

        self.label = Label(master, text="Do you prefer to room with male or female?")
        self.label.pack()

        self.male_button = Button(master, text="Male", command=self.assignMale)
        self.male_button.pack()
        self.female_button = Button(master, text="Female", command=self.assignFemale)
        self.female_button.pack()

        self.label = Label(master, text="On average, what time do you go to sleep? \n(1 = before 10pm, 2 = 10pm-12am, 3 = after 12am): ")
        self.label.pack()

        self.one_button = Button(master, text="1", command=self.assign1)
        self.one_button.pack()
        self.two_button = Button(master, text="2", command=self.assign2)
        self.two_button.pack()
        self.three_button = Button(master, text="3", command=self.assign3)
        self.three_button.pack()

        self.label = Label(master, text="On average, what time do you wake up? \n(1 = before 10pm, 2 = 10pm-12am, 3 = after 12am): ")
        self.label.pack()

        self.one_button = Button(master, text="1", command=self.assign1)
        self.one_button.pack()
        self.two_button = Button(master, text="2", command=self.assign2)
        self.two_button.pack()
        self.three_button = Button(master, text="3", command=self.assign3)
        self.three_button.pack()

        self.save_button = Button(master, text='Save', command = master.quit)
        self.save_button.pack()

    def assignMale(self):
        print("m", end =' ')
    def assignFemale(self):
        print("f", end =' ')
    def assign1(self):
        print(1, end =' ')
    def assign2(self):
        print(2, end =' ')
    def assign3(self):
        print(3, end =' ')
    def assign4(self):
        print(4, end =' ')
    def assign5(self):
        print(5, end =' ')
    def assignY(self):
        print('Y', end=' ')
    def assignN(self):
        print('N', end=' ')

root = Tk()
my_gui = MyFirstGUI(root)
root.mainloop()

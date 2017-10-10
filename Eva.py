# a program that is going to create difference kinds of "people" used in
# roomate paring
# creating a people class
import random
class people:
    # assign different characteristics to the people
    def __init__(self):
        e = ["Stack", "Overflow", "rocks"]
        self.nameVal = random.choice(e)

        self.sleepVal = random.randint(1,3)
        
        self.wakeVal = random.randint(1,3)
        
        smokingExpectation = ["S","N"]
        self.smokeVal = random.choice(smokingExpectation)

        genderExpectation = ["F","M"]
        self.genderVal = random.choice(genderExpectation)

        gPreferExpectation = ["F","M"]
        self.gPreferVal = random.choice(gPreferExpectation)

        self.cleanVal = random.randint(1,5)

        self.guestsVal = random.randint(1,5)

        self.soundVal = random.randint(1,5)

    # fix it later for the requirements of phone number       
    def phonenumber(self):
        pass
        
    # turn the characeristic to a string
    def printout(self):
        result = ""
        result += (self.nameVal+str(self.sleepVal)+str(self.wakeVal)+self.smokeVal+self.genderVal+\
                  self.gPreferVal+str(self.cleanVal)+str(self.guestsVal)+str(self.soundVal))
        return result


# the main function, you can enter an arbitrary number
# and the random info will be generated in a file called textfile.txt
def main():
    
    # uncomment the line above if you want to erase the original data
    # open("filename","w").close()
    
    file = open("textfile.txt","w")
    num = eval(input("Enter the number of person info you want to generate"))
    for i in range(0,num):
        newPerson = people()
        infoLine = newPerson.printout()
        file.write(infoLine)
        
    file.close()
    
main()

import math
import unittest

# this class represents each person's traits and preferences
class Person ():

    def __init__(self, id, firstName, lastName, wakingTime, bedtime, smoker, gender, preferredRoommateGender, cleanliness, guestComfort, loudness):
        self.firstName = firstName
        self.lastName = lastName
        self.id = id
        self.gender = gender
        self.preferredRoommateGender = preferredRoommateGender
        self.wakingTime = int(wakingTime)
        self.bedtime = int(bedtime)
        self.cleanliness = int(cleanliness)
        self.guestComfort = int(guestComfort)
        self.loudness = int(loudness)
        self.smoker = (smoker)

# this class creates an object that holds all the people in a list
class People ():

    def __init__(self):
        self.people = []

    def addPerson(self, person):
        self.people.append(person)

    def removePerson(self, id):
        for i in range (len(self.people)):
            print (i)
            if self.people[i].id == id:
                self.people.pop(i)
                break

    def populatePeople(self, infile):
        for line in infile:
            newPersonData = line.split()
            self.addPerson(Person(newPersonData[0],newPersonData[1],newPersonData[2],newPersonData[3],newPersonData[4],newPersonData[5],newPersonData[6], newPersonData[7],newPersonData[8],newPersonData[9], newPersonData[10]))

    #override the equal and not equal functions for later unit testing
    def __eq__(self, other):
        return self.people == other.people

    def __ne__(self, other):
        return not self.people == other.people


def main():
        roommateList = People()
        infile = open("Roommates.txt", "r")
        roommateList.populatePeople(infile)
        yesCheck = ["Y", "y", "Yes", "yes", "YES"]
        noCheck = ["N", "n", "No", "no", "NO"]
        maleGenderCheck = ["M","m","Male","male","MALE"]
        femaleGenderCheck = ["F","f","Female","female","FEMALE"]


        '''
        end = False
        run = False

        while not end:
            run = str(input('Would you like to search for roommate matches? \n (Y or N): '))
            while run not in yesCheck or run not in noCheck:
                print ('Input not recognized.')
                run = str(input('Would you like to search for roommate matches? \n (Y or N): '))
            if run in yesCheck:
                roommateList.addNewUser()

            end = str(input('End program? '))
            if end in yesCheck:
                break
        '''



        # grab the most recent id number
        currentID = int(roommateList.people[-1].id)


        # prompt user for their information
        # unique info
        user_firstName = str(input("Enter your first name: "))
        user_lastName = str(input("Enter your last name: "))

        
        # relative questions
        user_cleanliness = int(input("On a scale of 1 to 5, how clean are you? \n(1= not clean, 5 = very clean): "))
        while user_cleanliness < 1 or user_cleanliness > 5:
            print ('Input out of range.')
            user_cleanliness = int(input("On a scale of 1 to 5, how clean are you? \n(1= not clean, 5 = very clean): "))

        user_guestComfort = int(input("\nOn a scale of 1 to 5, how comfortable are you with guests in the room? \n(1 = not comfortable, 5 = very comfortable): "))
        while user_guestComfort < 1 or user_guestComfort > 5:
            print ('Input out of range.')
            user_guestComfort = int(input("\nOn a scale of 1 to 5, how comfortable are you with guests in the room? \n(1 = not comfortable, 5 = very comfortable): "))

        user_loudness = int(input("\nOn a scale of 1 to 5, how comfortable with noise are you?\n(1 = not comfortable, 5 = very comfortable): "))
        while user_loudness < 1 or user_loudness > 5:
            print ('Input out of range.')
            user_loudness = int(input("\nOn a scale of 1 to 5, how comfortable with noise are you?\n(1 = not comfortable, 5 = very comfortable): "))
            

        # boolean questions
        user_smoker = input("\nAre you okay with smoking? \n(Y or N): ")
        while user_smoker not in yesCheck and user_smoker not in noCheck:
            print ('Input not recognized')
            user_smoker = input("\nAre you okay with smoking? \n(Y or N): ")
        if user_smoker in yesCheck:
            user_smoker = 'Y'
        else:
            user_smoker = 'N'

        user_gender = input("\nDo you identify as  male or female or N/A? \n(M, F): ")
        while user_gender not in maleGenderCheck and user_gender not in femaleGenderCheck:
            print ("Input not recognized.")
            user_gender = input("\nDo you identify as  male or female or N/A? \n(M, F): ")
        if user_gender in maleGenderCheck:
            user_gender = 'M'
        else:
            user_gender = 'F'

        user_preferredRoommateGender = input("\nDo you prefer to rooom with a  male or female? \n(M, F): ")
        while user_preferredRoommateGender not in maleGenderCheck and user_preferredRoommateGender not in femaleGenderCheck:
            print ("Input not recognized.")
            user_preferredRoommateGender = input("\nDo you identify as male or female? \n(M, F): ")
        if user_preferredRoommateGender in maleGenderCheck:
            user_preferredRoommateGender = 'M'
        else:
            user_preferredRoommateGender = 'F'


        # discrete questions
        user_bedtime = int(input("\nOn average, what time do you go to sleep? \n(1 = before 10pm, 2 = 10pm-12am, 3 = after 12am): "))
        user_wakingTime = int(input("\nOn average, what time do you wake up? \n(1 = before 7am, 2 = 7am-9am, 3 = after 9am: "))

        # initialize the person object for the new user
        newUser = Person(currentID + 1, user_firstName, user_lastName, user_wakingTime, user_bedtime, user_smoker, user_gender, user_preferredRoommateGender, user_cleanliness, user_guestComfort, user_loudness)

        matchScore = 1000000000
        matches = []
        for person in roommateList.people:
            if person.smoker == newUser.smoker and person.gender == newUser.preferredRoommateGender and person.preferredRoommateGender == newUser.gender:
                score = math.sqrt(pow(newUser.wakingTime - person.wakingTime, 2) + pow(newUser.bedtime - person.bedtime, 2) + pow(newUser.cleanliness - person.cleanliness, 2) + pow(newUser.guestComfort - person.guestComfort, 2) + pow(newUser.loudness - person.loudness, 2))
                if score < matchScore:
                    matchScore = score
                    matches = []
                    matches.append (person)
                elif score == matchScore:
                    matches.append(person)

        for match in matches:
            print (match.firstName + ' ' + match.lastName)

        # prompt user whether or not they would like to be added to the database
        userJoinDatabase = str(input("Would you like to add yourself to the roommate databse? \n(Y or N): "))

        roommateList.addPerson(newUser)

#main()

class TestSortRoomates(unittest.TestCase):
    infile = open('Roommates.txt','r')

    # test the creation of a People object
    testDatabase = People()
    def testCreatePeople(self):
        assert self.testDatabase is not None

    def testPeoplePopulate(self):
        unpopulatedDatabase = People()
        self.testDatabase.populatePeople(self.infile)
        self.assertNotEqual(self.testDatabase, unpopulatedDatabase)

    # test the creation of a Person
    testPerson = Person(5000, 'Nikola', 'Tesla', 3, 3, 'N', 'M', 'M', 2, 2, 2)
    def testCreatePerson(self):
        assert self.testPerson is not None

    # test adding a Person object to a People object database
    def testPeopleAddPerson(self):
        self.testDatabase.addPerson(self.testPerson)
        self.assertEqual(self.testDatabase.people[-1], self.testPerson)

    # test the removal of a Person object from a People database
    def testPeopleRemovePerson(self):
        firstPersonInDatabase = self.testDatabase.people[0]
        self.testDatabase.removePerson(firstPersonInDatabase.id)
        newFirstPersonInDatabase = self.testDatabase.people[0]       
        self.assertNotEqual(firstPersonInDatabase, newFirstPersonInDatabase)


if __name__ == '__main__':
    unittest.main()


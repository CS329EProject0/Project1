import math
import unittest
import operator
import tkinter


# this class represents each person's traits and preferences
class Person ():

	def __init__(self, id, firstName, lastName, wakingTime, bedtime, smoker, drinker, \
	studyLoc, studyHrs, tvHrs, allNight, gender, preferredRoommateGender, cleanliness, guestComfort, loudness):
		self.firstName = firstName
		self.lastName = lastName
		self.id = int(id)
		self.gender = gender
		self.preferredRoommateGender = preferredRoommateGender
		self.wakingTime = int(wakingTime)
		self.bedtime = int(bedtime)
		self.cleanliness = int(cleanliness)
		self.guestComfort = int(guestComfort)
		self.loudness = int(loudness)
		self.smoker = smoker
		self.drinker = drinker
		self.studyLoc = studyLoc
		self.studyHrs = int(studyHrs)
		self.tvHrs = int(tvHrs)
		self.allNight = int(allNight)

	def __str__(self):
		return (self.firstName + " " + self.lastName)

	def dataReturn (self):
		return (str(self.id) + " " + self.firstName + " " + self.lastName + " " + str(self.wakingTime) + " " + str(self.bedtime) + " " + self.smoker + " " + self.drinker + " " + \
		self.studyLoc + " " + str(self.studyHrs) + " " + str(self.tvHrs) + " " + str(self.allNight) + " " + self.gender + " " + self.preferredRoommateGender + " " + str(self.cleanliness) + " " + \
		str(self.guestComfort) + " " + str(self.loudness))

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
			self.addPerson(Person(newPersonData[0],newPersonData[1],newPersonData[2],newPersonData[3],newPersonData[4],newPersonData[5], \
				newPersonData[6], newPersonData[7],newPersonData[8],newPersonData[9], newPersonData[10], newPersonData[11], newPersonData[12], \
				newPersonData[13], newPersonData[14], newPersonData[15]))


	def size(self):
		return len(self.people)

	 # override the equal and not equal functions for later unit testing
	def __eq__(self, other):
		return self.people == other.people

	def __ne__(self, other):
		return not self.people == other.people

	def __str__(self):
		returnstr = ''
		for person in self.people:
			returnstr += str(person) + '\n'
		return returnstr

	def createNewUser(self, currentID):
		newUserInfile = open("newUserTemp.txt","r")
		newUserData = newUserInfile.readline().split()
		newUser = Person(currentID, newUserData[0], newUserData[1],newUserData[2],newUserData[3],newUserData[4],newUserData[5], \
				newUserData[6], newUserData[7],newUserData[8],newUserData[9], newUserData[10], newUserData[11], newUserData[12], \
				newUserData[13], newUserData[14])
		return newUser

	# conducts survey and finds matches for user, then adds user to database if desired
	# NOTE: this was the originial method by which we conducted the survey, however it is
	# now conducted via the GUI
	def testAddNewUser (self):
		yesCheck = ["Y", "y", "Yes", "yes", "YES"]
		noCheck = ["N", "n", "No", "no", "NO"]
		maleGenderCheck = ["M","m","Male","male","MALE"]
		femaleGenderCheck = ["F","f","Female","female","FEMALE"]

		# grab the most recent id number
		currentID = int(self.people[-1].id) + 1

		# prompt user for their information
		# unique info
		user_firstName = str(input("Enter your first name: "))
		while not user_firstName.isalpha() or ' ' in user_firstName:
			print ('Input not recognized.')
			user_firstName = str(input("Enter your first name: "))

		user_lastName = str(input("Enter your last name: "))
		while not user_lastName.isalpha() or ' ' in user_lastName:
			print ('Input not recognized.')
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
			user_smoker = 'S'
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

		user_preferredRoommateGender = input("\nDo you prefer to room with a male or female? \n(M, F): ")
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
		newUser = Person(currentID, user_firstName, user_lastName, user_wakingTime, user_bedtime, user_smoker, user_gender, user_preferredRoommateGender, user_cleanliness, user_guestComfort, user_loudness)

	def searchForMatches(self, newUser):
		# use these to check user input
		yesCheck = ["Y", "y", "Yes", "yes", "YES"]
		noCheck = ["N", "n", "No", "no", "NO"]

		# parse the roommate database for matches
		roommateScores = {}
		for person in self.people:
			# filter results for smoking and gender preferences of user and potential roommate
			if person.smoker == newUser.smoker and person.gender == newUser.preferredRoommateGender and person.preferredRoommateGender == newUser.gender and newUser.drinker == person.drinker:
				roommateScores[person] = math.sqrt(pow(newUser.wakingTime - person.wakingTime, 2) + pow(newUser.bedtime - person.bedtime, 2) + \
					pow(newUser.cleanliness - person.cleanliness, 2) + pow(newUser.guestComfort - person.guestComfort, 2) + \
					pow(newUser.loudness - person.loudness, 2) + pow(newUser.studyHrs - person.studyHrs, 2) + \
					pow(newUser.tvHrs - person.tvHrs, 2) + pow(newUser.allNight - person.allNight, 2))
				
		sorted_roommates = sorted(roommateScores.items(), key = operator.itemgetter(1))
		matches = sorted_roommates[:10]
				
		# print out matches
		print ('\n' + str(newUser) + ', we found '+str(len(matches)) + ' roommate(s) matching your preferences in our database:')
		print ()

		percentMatchModifier = 12.126781251816649
		for i in range(len(matches)):
			print("Name: " + '{:25s}'.format(str(matches[i][0])) + "Percent Match: " +  '{:2.2f}'.format(100 - (percentMatchModifier * matches[i][1])) + '%')

		# prompt user whether or not they would like to be added to the database
		userJoinDatabase = str(input("\nWould you like to add yourself to the roommate database? \n(Y or N): "))
		if userJoinDatabase in yesCheck:
			roommateDatabase = open("Roommates.txt", "a")
			roommateDatabase.write(newUser.dataReturn() + '\n')
			roommateDatabase.close()
			self.addPerson(newUser)
			print ("\nYou have been successfully added to the database.")

			# close the database file
			roommateDatabase.close()


def main():
		# import the gui file
		import GuiReader
		from GuiReader import GUI

		# initialize roommate database
		roommateList = People()
		infile = open("Roommates.txt", "r")
		roommateList.populatePeople(infile)

		# initialize the current id number
		currentID = (roommateList.people[-1].id) + 1

		# use these to check user input
		yesCheck = ["Y", "y", "Yes", "yes", "YES"]
		noCheck = ["N", "n", "No", "no", "NO"]


		# initialize flags to keep program continuous
		end = False

		# prompt user to search 
		run = str(input('Would you like to search for roommate matches? \n(Y or N): '))
		while run not in yesCheck and run not in noCheck:
			print ('\nInput not recognized.')
			run = str(input('Would you like to search for roommate matches? \n(Y or N): '))
		if run in yesCheck:
			root = tkinter.Tk()
			displayGUI = GUI(root)
			root.mainloop()

			# grab the new user as a Person object
			newUser = roommateList.createNewUser(currentID)
			currentID += 1
			# search for matches
			roommateList.searchForMatches(newUser)

		else:
			end = True

		while not end:
			endCheck = str(input('\nWould you like to search for roommate matches for another user? \n(Y or N): '))
			while endCheck not in yesCheck and endCheck not in noCheck:
				print ('\nInput not recognized.')
				endCheck = str(input('\nWould you like to search for roommate matches for another user? \n(Y or N): '))
			if endCheck in noCheck:
				end = True
			else:
				root = tkinter.Tk()
				displayGUI = GUI(root)
				root.mainloop()

				# grab the new user as a Person object
				newUser = roommateList.createNewUser(currentID)
				currentID += 1
				# search for matches
				roommateList.searchForMatches(newUser)

		# close the text in-file
		infile.close()

main()

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
	testPerson = Person(9001, 'Nikola', 'Tesla', 3, 3, 'N', 'N', 'Y', 2, 2, 2, 'M', 'M', 3, 1, 2)
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

	def testPeopleSize (self):
		exogenousSize = len(self.testDatabase.people)
		self.assertEqual(exogenousSize, self.testDatabase.size())

	def testPeople__str__ (self):
		peopleDatabaseStr = ''
		for i in range (len(self.testDatabase.people)):
			peopleDatabaseStr += self.testDatabase.people[i].firstName + ' ' + self.testDatabase.people[i].lastName +'\n'
		self.assertEqual(peopleDatabaseStr, str(self.testDatabase))

	def testPersonDataReturn (self):
		self.assertEqual(self.testPerson.dataReturn(), '9001 Nikola Tesla 3 3 N N Y 2 2 2 M M 3 1 2')


if __name__ == '__main__':
	unittest.main()

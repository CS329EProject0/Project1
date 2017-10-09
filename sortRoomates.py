import math

# this class represents each person's traits and preferences
class Person ():

	def __init__(self, firstName, lastName, id, gender, preferredRoomateGender, wakingTime, bedtime, cleanliness, guestComfort, loudness):
		self.firstName = firstName
		self.lastName = lastName
		self.id = id
		self.gender = gender
		self.preferredRoomateGender = preferredRoomateGender
		self.wakingTime = int(wakingTime)
		self.bedtime = int(bedtime)
		self.cleanliness = int(cleanliness)
		self.guestComfort = int(guestComfort)
		self.loudness = int(loudness)

# this class creates an object that holds all the people in a list
class People ():

	def __init__(self):
		self.people = []

	def addPerson(self, person):
		self.people.append(person)

	def removePerson(self, id):
		for i in range (self.people):
			print (i)
			if self.people[i].id == id:
				self.people.pop(i)
				break

# Create the people database object and populate it
def main():
        roommateList = People()
        infile = open("Roomates.txt", "r")
        for line in infile:
                newPersonData = line.split()
                print(newPersonData)
                newPerson = Person(newPersonData[0], newPersonData[1], newPersonData[2], newPersonData[3], newPersonData[4], newPersonData[5], newPersonData[6], newPersonData[7], newPersonData[8], newPersonData[9])
                roommateList.people.append(newPerson)

        # the higher the score, the more difference the two people are
        totalScore = 0 

        # relative questions
        user_cleanliness = int(input("On a scale of 1 to 5, how clean are you? \n(1= not clean, 5 = very clean): "))
        user_guestComfort = int(input("\nOn a scale of 1 to 5, how comfortable are you with guests in the room? \n(1 = not comfortable, 5 = very comfortable): "))
        user_loudness = int(input("\nOn a scale of 1 to 5, how comfortable with noise are you?\n(1 = not comfortable, 5 = very comfortable): "))

        # boolean questions
        user_smoker = input("\nAre you okay with smoking? \n(Y or N): ")
        user_gender = input("\nDo you identify as  male or female or N/A? \n(M, F, or N/A): ")
        user_preferredRoomateGender = input("\nDo you prefer to rooom with a  male or female or N/A? \n(M, F, or N/A): ")

        # discrete questions
        user_bedtime = int(input("\nOn average, what time do you go to sleep? \n(1 = before 10pm, 2 = 10pm-12am, 3 = after 12am): "))
        user_wakingTime = int(input("\nOn average, what time do you wake up? \n(1 = before 7am, 2 = 7am-9am, 3 = after 9am: "))

        for person in roommateList.people:
                totalScore += math.sqrt(pow((user_cleanliness - person.cleanliness), 2) + pow((user_guestComfort - person.guestComfort), 2) + \
                                   pow((user_loudness - person.loudness), 2) + pow((user_bedtime - person.bedtime), 2) + \
                                   pow((user_wakingTime - person.wakingTime), 2))

        print(totalScore)
main()



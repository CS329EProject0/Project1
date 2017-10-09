# this class represents each person's traits and preferences
class Person ():

	def __init__(self, firstName, lastName, id, sex, preferredRoomateSex, wakingTime, bedtime, relCleanliness, relGuests, relLoudness):
		self.firstName = firstName
		self.lastName = lastName
		self.id = id
		self.sex = sex
		self.preferredRoomateSex = preferredRoomateSex
		self.wakingTime = wakingTime
		self.bedtime = bedtime
		self.relCleanliness = relCleanliness
		self.relGuests = relGuests
		self.relLoudness = relLoudness

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
	People = People()
	infile = open("Roomates.txt", "r")
	while infile:
		newPersonData = infile.readline().split()
		newPerson = Person(newPersonData[0], newPersonData[1], newPersonData[2], newPersonData[3], newPersonData[4], newPersonData[5], newPersonData[6], newPersonData[7], newPersonData[8], newPersonData[9])
		People.append(newPerson)


main()




# this class represents each persons traits and preferences
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

def main():
	People = People()
	infile = open("Roomates.txt", "r")
	while infile:
		newPerson = 


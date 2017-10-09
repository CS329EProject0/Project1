def main():
        totalScore = 0 

        # relative questions
	cleanliness = int(input("On a scale of 1 to 5, how clean are you? \n(1= not clean, 5 = very clean): "))
	peopleComfort = int(input("On a scale of 1 to 5, how comfortable are you with guests in the room? \n(1 = not comfortable, 5 = very comfortable): "))
	loudness = int(input("On a scale of 1 to 5, how comfortable with noise are you?\n(1 = not comfortable, 5 = very comfortable): "))

	# boolean questions
	smoker = eval(input("Are you okay with somking? \n(Y or N): "))
	gender = eval(input("Do you identify as  male or female or N/A? \n(M, F, or N/A): "))
	genPref = eval(input("Do you prefer to rooom with a  male or female or N/A? \n(M, F, or N/A): "))
	
	# discrete questions
	sleep = eval(input("On average, what time do you go to sleep? \n(1 = before 10pm, 2 = 10pm-12am, 3 = after 12am): "))
	wakeUp = eval(input("On average, what time do you wake up? \n(1 = before 7am, 2 = 7am-9am, 3 = after 9am"))

	for person in linkedlist:
                calculate totalScore
	
main()

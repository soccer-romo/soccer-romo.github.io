import random

user_variable = 0
chances = 2
user_answer = "yes"

while (user_answer == "yes" or user_answer == "y"):
	my_number = random.randrange(0,11)
	chances = 2
	user_variable = int(input("Guess my number between 0 and 10. You get three chances: "))
	if (user_variable == my_number):
		print("Good Job! You've guessed my number")
	while (user_variable == range(0,11)):
		pass
		if(user_variable != my_number):
			user_variable = int(input("Too bad! Try again! "))
			chances -= 1
		elif(user_variable == my_number):
			print("Good Job! You've guessed my number!")
			break
		elif (chances == 0):
			print("Game Over. My number was " + str(my_number))
			break


user_answer = input("Do you want to play again? ").lower()

while(user_answer != "yes" and user_answer != "y" and user_answer != "no" and user_answer != "n"):
	user_answer = input("Please enter in yes or no: ")
	if (user_answer == "no" or user_answer == "n"):
		print("Thank you for playing!")
		break	
#Modify the Guess My Number game so that the player has a limited number of guesses. If the player fails to guess in time, the program should display an appropriately chastising message.
#Psudocode
#delcare my_number #set varible to = whatever the user inputs
#add chances
#Set loop i
#import random
import random

user_variable = 0
chances = 2
user_answer = "yes"

while (user_answer == "yes" or user_answer == "y"):
	my_number = str(random.randrange(0,11))
	chances = 2
	user_variable = input("Guess my number between 0 and 10. You get three chances: ")
	if (user_variable == my_number):
		print("Good Job! You've guessed my number")
	while (user_variable != my_number):
		user_variable = input("Too bad! Try again! ")
		chances -= 1
		if(user_variable == my_number):
			print("Good Job! You've guessed my number!")
			break
		if (chances == 0):
			print("Game Over. My number was " + str(my_number))
			break


        user_answer = input("Do you want to play again? ").lower()

        while(user_answer != "yes" and user_answer != "y" and user_answer != "no" and user_answer != "n"):
                user_answer = input("Please enter in yes or no: ")
        if (user_answer == "no" or user_answer == "n"):
                print("Thank you for playing!")
                break

#Improve the function ask_number() so that the function can be called with a step value. Make the default value of step 1.
#Modify the Guess My Number chapter project from Chapter 3 by reusing the function ask_number().
#Modify the new version of Guess My Number you created in the last challenge so that the program's code is in a function called main(). Don't forget to call main() so that you can play the game.
#Write a new computer_move() function for the Tic-Tac-Toe game to plug the hole in the computer's strategy. See if you can create an opponent that is unbeatable!


#3)

import random

def ask_number(question, low, high): 
	"""Ask for a number within a range.""" 
	response = None while response not in range(low, high): 
	response = int(input(question))
	return response

user_guess = input("Guess my number between 0 and 10. You get three chances: ")


def guess_my_number(user_variable):
	chances = 2
	user_answer = "yes"

	while (user_answer == "yes" or user_answer == "y"):
		my_number = str(random.randrange(0,11))
		chances = 2
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


guess_my_number(ask_number())

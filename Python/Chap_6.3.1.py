#Modify the Guess My Number chapter project from Chapter 3 by reusing the function ask_number().
#Modify the new version of Guess My Number you created in the last challenge so that the program's code is in a function called main(). Don't forget to call main() so that you can play the game.
#Write a new computer_move() function for the Tic-Tac-Toe game to plug the hole in the computer's strategy. See if you can create an opponent that is unbeatable!


#2 and  #3)

import random
def main():
	print("""Hi! This is a guess the number game. In this game you will first select a 
	range for which you want to guess. Then the computer will randomly generate 
	a number for you. It'll then see if the numbers match up. If not you
	get to pick the number to try and guess it for your self. You also only
	have 3 chances. GoodLuck!
	""")

	def ask_number(low, high, step = 1):
		low_num = low
		high_num = high + 1
		step = step
		num_range = random.randrange(low_num,high_num,step)
		return num_range
		
	low = int(input("What number do you want you lowest number to be? "))
	high = int(input("What number do you want you highest number to be? "))


	def guess_my_number(user_variable):
		chances = 2
		user_answer = "yes"
		user_variable = user_variable
		
		while (user_answer == "yes" or user_answer == "y"):
			my_number = str(random.randrange(low,high + 1))
			chances = 2
			if (user_variable == my_number):
				print("Good Job! You've guessed my number")
			while (user_variable != my_number):
				user_variable = input("The range is in between " + str(low) + " and " + str(high) + ". It's your turn to guess.")
				chances -= 1
				if(user_variable == my_number):
					print("Good Job! You've guessed my number!")
					break
				if (chances == 0):
					print("Game Over. My number was " + str(my_number))
					break


			user_answer = input("Do you want to play again? ").lower()
			if (user_answer == "yes" or user_answer == "y"):
				user_variable = str(input("What do you want your next guess to be? "))
				continue

			if (user_answer == "no" or user_answer == "n"):
					print("Thank you for playing!")
					break

	user_variable = (ask_number(low, high))
	print("Your random generated number is: " + str(user_variable))
	guess_my_number(user_variable)

main()
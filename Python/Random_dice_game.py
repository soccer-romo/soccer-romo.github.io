#dice Game
import random
user_guess = 0
user_guess_again = "yes"

print("Welcome to the OTC CIS 120 Casino!")

while(user_guess_again == "yes" or user_guess_again == "y"):
	while (user_guess == 0 or (user_guess < 2 or user_guess > 12) ):
		try:
	 		user_guess = int(input("Please enter a number between 2 and 12: "))
		except:
			#print("Not a number!")
			continue
			
	print("You've guessed " + str(user_guess))
	die1= random.randint(1,6)
	die2 = random.randint(1,6)
	print("Die 1: " + str(die1))
	print("Die 2: " + str(die2)) 
	
	
	if (user_guess == die1 + die2):
		print("You guessed correctly!")
	else:
		print("You guessed incorrectly")
	
		
	user_guess_again = input("Do you want to guess again?").lower
	while (user_guess_again != "yes" or user_guess_again != "y" or user_guess_again != "no" or user_guess_again != "n"):
		print("Please type in (y) or (n)")
	else:
		break
user_guess = 0
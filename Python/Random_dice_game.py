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
			print("Not a number!")
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
	
		
	user_guess_again = input("Do you want to guess again? ")
	while (user_guess_again != "yes" and user_guess_again != "y" and user_guess_again != "no" and user_guess_again != "n"):
		user_guess_again = input("Please enter a yes(y) or no(n)")
	if (user_guess_again == "yes" or user_guess_again == "y"):
		user_guess = int(input("Please enter a number between 2 and 12: "))
	elif(user_guess_again == "no" or user_guess_again == "n"):
		print("Thank you for playing!")
		break
		
user_guess = 0
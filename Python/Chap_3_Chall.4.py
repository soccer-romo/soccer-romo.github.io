# Here's a bigger challenge. Write the pseudocode for a program where the player and the computer trade places in the number guessing game. That is, the player picks a random number between 1 and 100 that the computer has to guess. Before you start, think about how you guess. If all goes well, try coding the game.
# Declare user_number
#declare computer_number
import random
user_number = 0
computer_number = 0 
points = 0 
user_range = list(range(0,11))
user_number = int(input("What number would you like for the computer to guess from 0 to 100? "))

computer_number = random.randrange(0,101)

while (computer_number != user_number):
	computer_number = random.randrange(1,101)
	points += 1
	print(computer_number)
	pass
	if(computer_number == user_number):
		print("Your number reached: " + str(points) + " point")
		if (points <= 100):
			print ("You lost")
		elif(points >= 100):
			print("You've won!")

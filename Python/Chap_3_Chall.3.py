#Modify the Guess My Number game so that the player has a limited number of guesses. If the player fails to guess in time, the program should display an appropriately chastising message.
#Psudocode
#delcare my_number
#set varible to = whatever the user inputs
#add chances
#Set loop
import random

my_number = random.randrange(0,11)

range_num = str(list(range(0,101)))
user_variable = 0
chances = 2
string = ""

print(my_number)

user_variable = input("Guess my number between 0 and 10. You get three chances: ")

if (user_variable != range_num):
	

if (user_variable == my_number):
	print("Good Job! You guessed my number!")

while (user_variable != my_number):
	user_variable = int(input("Too bad! Try again!"))
	chances -= 1
	if (user_variable == my_number):
		print("Good Job! You guessed my number!")
		break
	if (chances == 0):
		print("Game Over. My number was " + str(my_number))
		break
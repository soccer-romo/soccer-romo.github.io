input("There are four games to choose from. Which do you want from 1-4: ")





def funtion_1():
	import random
	fortune = random.randrange(1,6)

	fortune_1 = "You'll have a great day today!"
	fortune_2 = "You'll meet a new special friend soon!"
	fortune_3 = "7 is your lucky number today!"
	fortune_4 = "If you work hard today. You'll find a good treasure!"
	fortune_5 = "You're unlucky today."

	print ("Here is your fortune for today: ")
	if (fortune == 1):
		print (fortune_1)
	elif (fortune == 2):
		print(fortune_2)
	elif (fortune == 3):
		print(fortune_3)
	elif (fortune == 4):
		print(fortune_4)
	elif (fortune == 5):
		print(fortune_5)
			
	print("Have a great day!")

def funtion_2():
	import random

	head_count = 0
	tail_count = 0
	total_flip = 0

	while (total_flip <= 99):
		flip = random.randrange(1,3)
		if (flip == 1):
			head_count += 1
			total_flip += 1
		elif (flip == 2):
			tail_count += 1
			total_flip += 1

	print("Head Count: " + str(head_count) + " flips")	
	print("Tail Count: " + str(tail_count) + " flips")
	
def funtion_3():
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
def funtion_4():
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
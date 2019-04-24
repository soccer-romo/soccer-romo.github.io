import random

#Starting the loop
user_finish = "yes"
user_points = 0

#getting everything under the loop to have user stay in if they choose to do so
while(user_finish == "yes" or user_finish == "y"):
	random_num = random.randrange(0,4)

#	These are the word jumble with the hints respectivly with it
	questions= ["1","2","3","4"]
	answers = ["5","6","7","8"]
	options_to_give = ["5","6","7","8"]
	
	question_given = questions[random_num]
	answer = answers[random_num]
	options = options_to_give[random_num]
#	print(question)
	print(question_given)

#	User's word for guess
	user_answer = input("""...""").lower()

#	loop for user's answer
	while (user_answer != answer):
		print ("Here are your Options")
		for option in options_to_give:
			print(option)
		user_answer = input("Guess again!").lower()
	else:
		print("Good Job! You've guessed the word!")
		user_points += 2
		print("Points: " + str(user_points))
		user_points = int(user_points)
			
	user_finish = input("Do you want to play again? ").lower()
	if (user_finish == "yes" or user_finish == "y"):
		continue
	elif (user_finish == "no" or user_finish == "n"):
		break
	else:
		user_finish = input("Please type in yes or no. ")

print("Thank you for playing!")
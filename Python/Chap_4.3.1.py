# 3. Improve "Word Jumble" so that each word is paired with a hint. The player should be able to see the hint if he or she is stuck. Add a scoring system that rewards players who solve a jumble without asking for the hint.
#puesdocode
#make an array of words for the player to choose from
#add hints to words
import random

#Starting the loop
user_finish = "yes"
user_points = 0

#getting everything under the loop to have user stay in if they choose to do so
while(user_finish == "yes" or user_finish == "y"):
	random_num = random.randrange(0,14)

#	These are the word jumble with the hints respectivly with it
	word_jumble = ["red","blue","yellow","cheetah","lion","jaguar","house cat","tiger","infant","baby","toddler", "child", "teen","adult"]
	hints = ["Usually associated with war","Usually asscociated with calm and peace","Usually asscociated with speed","It's the fastest land mammal","The pride of the jungle","Usually kills by aiming for the neck","lives in a house","Was an evil charcter in mowgli","Youngest stage","Starts crawling and walking in life","Starts talking in life","Starts school in life","Enter jr. high in life","Starts college and getting married in life",]

	word_to_guess = word_jumble[random_num]
	hint_to_give = hints[random_num]
#	print(word_to_guess)

#	User's word for guess
	user_word = input("""This is a word game. 
You have to guess between the three primary colors, type of cat, and the stages of a human life between infant and adult. 
GoodLuck!
What is the word you want to guess? """).lower()

#	loop for user's word
	while (user_word != word_to_guess):
		print ("Here is your hint: " + hint_to_give)
		user_word = input("Guess again!").lower()
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
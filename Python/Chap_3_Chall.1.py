# Write a program that simulates a fortune cookie. The program should display on of five unique fortunes, at random, each time it's run.
#pesdocode 
#import random
#set range 1-5
#first label 5 fortune cooks.

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
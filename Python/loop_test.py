#loop test
user_exit = "no"

while (user_exit == "no" or user_exit == "n"):
	print ("Hi")
	user_exit = (input("Do you want to exit?")).lower()

user_input = input("How many cars do you want to buy? ")

while ((int(user_input)) < 1 or (int(user_input)) > 15):
	user_input = input("How many cars do you want to buy? (At least one and not more than 15.) ")
print("Thanks for your purchase!")
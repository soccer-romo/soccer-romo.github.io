menuItems = []
userExit = False

while(userExit == False):
	item = input("Please enter an item to add to the menu: ")
	menuItems.append(item)
	userinput = input("Do you want to add additional items to the menu? ")
	if (userinput == "no" or userinput == "n"):
		userExit = True

print(menuItems)

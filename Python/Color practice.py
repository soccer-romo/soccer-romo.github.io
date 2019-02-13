#allow user to pick a team color. Test the color to determine if it is a primary color

color = (input("Enter a color: ")).lower()

choice = True

# Check which team color was chosen
if color == "red":
	print("Welcome to team Red!")
elif color == "green":
	print("Welcome to team Green!")
elif color == "blue":
	print("Welcome to team Blue!")
else:
	print ("Not team Red, Blue, Green.")
	
#check for primary color

if color == "red" or color == "yellow" or color == "blue":
	print ("You have choosen a primary color.")

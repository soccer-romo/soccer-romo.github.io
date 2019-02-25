#declare varibles
num_quarters = 0 
num_dimes = 0
num_nikels = 0 
num_pennies = 0 
amount_of_change = 0 

amount_of_change = int(input("How much change do you want? "))

while(amount_of_change > 0):
	
	if (amount_of_change >= 25):
		num_quarters = num_quarters + 1
		amount_of_change = amount_of_change - 25
		continue
	elif (amount_of_change >= 10):
		num_dimes = num_dimes + 1 
		amount_of_change = amount_of_change - 10
	
	elif (amount_of_change >= 5):
		num_nikels = num_nikels + 1
		amount_of_change = amount_of_change - 5
	
	elif (amount_of_change >= 1):
		num_pennies = num_pennies + 1
		amount_of_change = amount_of_change - 1
	else:
		break

'''
while (amount_of_change >= 25):
	num_quarters = num_quarters + 1
	amount_of_change = amount_of_change - 25
	
while (amount_of_change >= 10):
	num_dimes = num_dimes + 1 
	amount_of_change = amount_of_change - 10
	
while (amount_of_change >= 5):
	num_nikels = num_nikels + 1
	amount_of_change = amount_of_change - 5

while (amount_of_change >= 1):
	num_pennies = num_pennies + 1
	amount_of_change = amount_of_change - 1
'''
	
	
#end while
print("Your change: ")
print("Quarters: " + str(num_quarters))
print("Dimes: " + str(num_dimes))
print("Nickels: " + str(num_nikels))
print("Pennies: " + str(num_pennies))


while(True):
	userinput = input("Do you want to exit? ")
	if (userinput == "yes"):
		break
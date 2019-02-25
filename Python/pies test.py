#calculate discound on the purchase of multiple pies
number_of_pies = int(input("How many pies would you like to purchase? "))
total = 0 

#calculate discount

if number_of_pies >= 20:
	total = number_of_pies * 8
elif number_of_pies >= 10:
	total = number_of_pies * 9
elif number_of_pies > 0:
	total = number_of_pies * 10
else:
	print("Please enter a valid number of pies (more than zeros).")

#print out total cost
print ("Total Cost : $" + str(float(total)))
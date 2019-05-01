#pusdocode
#create module
#create class and define functions
#-----------------------------------
#functions needed
# 1) Have three arrays
#	a)engine type
#	b)vehicle type
#	c)color avalible
# 2) Have each vhicle type have it's own set of engines and color types
# 3) have user picking out what he/she wants
# 4) Spits out price for car
class intros():
	def intro1():
		print("Hi everyone! This is a car picking application where you get to pick a car that we have on the lot. Hope you enjoy shopping for the car of your dreams!")
	def intro2():
		print("First pick out the car you want by typing in the car's number that you want.")
	
	def intro3():
		print("Second pick out the engine size that you want from the car.")
	
	def intro4():
		print("Last but definitely not least. Pick out the colors you want from the color option.")
		
class carTypes(object):
	def cars():
		carChoices = {"1)":["Ford"],"2)":["Chevy"],"3)":["Dodge"],"4)":["Mercedes"],"5)":["Nissan"],"6)":["Subaru"],"7)":["Ferrari"]}
		for n,m in carChoices.items():
			print(n,m[0])
		carChoice = input("Number: ")
		return carChoice
	
	def engines():
		engineChoices = {"1)":["4-cylinder"],"2)":["V6"],"3)":["V8"],"4)":["V10"]}
		for n,e in engineChoices.items():
			print(n,e[0])
		engineChoice = input("Number: ")
		return engineChoice
		
	def colors():
		colorChoices = {"1)":["Black"],"2)":["Green"],"3)":["Blue"],"4)":["Yellow"],"5)":["Purple"],"6)":["Red"],"7)":["Orange"],"8)":["White"],"9)":["Brown"]}
		for n,c in colorChoices.items():
			print(n,c[0])
		colorChoice = input("Number: ")
		return colorChoice
		
class Prices():
	def car_price(car, total_price):
		car = car
		total_price = total_price
		if (car == "1"):
			total_price += 15000
			print("Total price so far: "+ str(total_price))
		elif (car == "2"):
			total_price += 17000
			print("Total price so far: "+ str(total_price))
		elif (car == "3"):
			total_price += 12000
			print("Total price so far: "+ str(total_price))
		elif (car == "4"):
			total_price += 30000
			print("Total price so far: "+ str(total_price))
		elif (car == "5" ):
			total_price += 10000
			print("Total price so far: "+ str(total_price))
		elif (car == "6"):
			total_price += 13000
			print("Total price so far: "+ str(total_price))
		elif (car == "7"):
			total_price += 70000
			print("Total price so far: "+ str(total_price))
		else:
			print("Not a good value.")
		return total_price
	
	def engine_prices(engine, total_price):
		engine = engine
		total_price = total_price
		if (engine == "1"):
			total_price += 1000
			print("Total price so far: "+ str(total_price))
		elif (engine == "2"):
			total_price += 2000
			print("Total price so far: "+ str(total_price))
		elif(engine == "3"):
			total_price += 3000
			print("Total price so far: "+ str(total_price))
		elif (engine == "4"):
			total_price += 4000
			print("Total price so far: "+ str(total_price))
		else:
			print("Not a value")
			engines = carTypes.option2(engines)
		return total_price
			
	def color_prices(color, total_price):
		color = color
		total_price = total_price
		if (color == "1"):
			total_price += 300
			print("Total price so far: "+ str(total_price))
		elif (color == "2"):
			total_price += 100
			print("Total price so far: "+ str(total_price))
		elif (color == "3"):
			total_price += 150
			print("Total price so far: "+ str(total_price))
		elif (color == "4"):
			total_price += 50
			print("Total price so far: "+ str(total_price))
		elif (color == "5"):
			total_price += 50
			print("Total price so far: "+ str(total_price))
		elif (color == "6"):
			total_price += 300
			print("Total price so far: "+ str(total_price))
		elif (color == "7"):
			total_price += 50
			print("Total price so far: "+ str(total_price))
		elif (color == "8"):
			total_price += 100
			print("Total price so far: "+ str(total_price))
		elif (color == "9"):
			total_price += 25
			print("Total price so far: "+ str(total_price))
		else:
			print("Not a value")
		return total_price

total_price = 0
def main():
	intros.intro1()
	intros.intro2()
	car = carTypes.cars()
	carPrice = Prices.car_price(car, total_price)

	intros.intro3()
	engine = carTypes.engines()
	enginePrice = Prices.engine_prices(engine, total_price)

	intros.intro4()
	color = carTypes.colors()
	colorPrice = Prices.color_prices(color, total_price)

	print("Your total price overall is: $" + str(carPrice + enginePrice + colorPrice))
	userExit = input("Do you still want to redo it? Type in yes or no: ").lower()

userExit = "yes"

while (userExit == "yes" or userExit == "y"):
	main()
	if (userExit == "no" or userExit == "n"):
		print("Thank you for using the app!")
		break
	else:
		userExit = input("Please type in yes or no: ").lower()
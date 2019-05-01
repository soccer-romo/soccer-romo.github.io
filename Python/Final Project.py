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
	def option1():
		carChoices = {"1)":["Ford"],"2)":["Chevy"],"3)":["Dodge"],"4)":["Mercedes"],"5)":["Nissan"],"6)":["Subaru"],"7)":["Ferrari"]}
		for n,m in carChoices.items():
			print(n,m[0])
		return 
	
	def option2():
		engineChoices = {"1)":["4-cylinder"],"2)":["V6"],"3)":["V8"],"4)":["V10"]}
		for n,e in engineChoices.items():
			print(n,e[0])
		return engineChoices
		
	def option3():
		colorChoices = {"1)":["Black"],"2)":["Green"],"3)":["Blue"],"4)":["Yellow"],"5)":["Purple"],"6)":["Red"],"7)":["Orange"],"8)":["White"],"9)":["Brown"]}
		for n,c in colorChoices.items():
			print(n,c[0])
		return colorChoices

class prices():
	def car_price(car, total_price):
		car = car
		if (car == "1"):
			total_price += 15000
		elif (car == "2"):
			total_price += 17000
		elif (car == "3"):
			total_price += 12000
		elif (car == "4"):
			total_price += 30000
		elif (car == "5" ):
			total_price += 10000
		elif (car == "6"):
			total_price += 13000
		elif (car == "7"):
			total_price += 70000
		else:
			print("Not a good value.")
	
	def engine_prices(engines, total_price):
		engines = engines
		total_price = total_price
		if (engines == "1"):
			total_price += 1000
		elif (engines == "2"):
			total_price += 2000
		elif(engines == "3"):
			total_price += 3000
		elif (engines == "4"):
			total_price += 4000
		else:
			print("Not a value")
			engines = carTypes.option2(engines)
			
	def color_prices(color, total_price):
		color = color
		total_price = total_price
		if (color == "1"):
			total_price += 300
		if (color == "2"):
			total_price += 100
		if (color == "3"):
			total_price += 150
		if (color == "4"):
			total_price += 50
		if (color == "5"):
			total_price += 50
		if (color == "6"):
			total_price += 300
		if (color == "7"):
			total_price += 50
		if (color == "8"):
			total_price += 100
		if (color == "9"):
			total_price += 25

total_price = 0

intros.intro1()
intros.intro2()
option1 = carTypes.option1()
intros.intro3()
option2 = carTypes.option2()
intros.intro4()
option3 = carTypes.option3()


#def pickingCar(cars):
	


	


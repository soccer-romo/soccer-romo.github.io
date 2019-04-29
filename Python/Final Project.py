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
	def carType():
		car_type = ["Ford","Chevy","Dodge","Mercedes","Nissan","Subaru","Ferrari"]
		return car_type

	def engineType():
		enging_type = ["4-cylinder","V6", "V8", "V10"]
		return enging_type
		
	def colorType():
		color_type = ["Black","Green","Blue","Yellow","Purple","Red","Orange","White","Brown"]
		return color_type
		
	def option1(cars):
		cars = cars
		carChoices = {"1)":["Ford"],"2)":["Chevy"],"3)":["Dodge"],"4)":["Mercedes"],"5)":["Nissan"],"6)":["Subaru"],"7)":["Ferrari"]}
		for n,m in carChoices.items():
			print(n,m[0])
		return 
	
	def option2(engines):
		engines = engines
		engineChoices = {"1)":["4-cylinder"],"2)":["V6"],"3)":["V8"],"4)":["V10"]}
		for n,e in engineChoices.items():
			print(n,e[0])
		return engineChoices
		
	def option3(colors):
		colors = colors
		colorChoices = {"1)":["Black"],"2)":["Green"],"3)":["Blue"],"4)":["Yellow"],"5)":["Purple"],"6)":["Red"],"7)":["Orange"],"8)":["White"],"9)":["Brown"]}
		for n,c in colorChoices.items():
			print(n,c[0])
		return colorChoices

cars = carTypes.carType()
engines = carTypes.engineType()
colors = carTypes.colorType()
intros.intro1()
intros.intro2()
option1 = carTypes.option1(cars)
intros.intro3()
option2 = carTypes.option2(engines)
intros.intro4()
option3 = carTypes.option3(colors)


#def pickingCar(cars):
	


	


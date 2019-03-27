#Recurison

def factiorial(n):
	if n == 1:
		return 1
	else:
		return n * factiorial(n-1)
print(factiorial(1))


#funtions

user_exit = False

def area_of_rectangle(lenght,height):
	area = int(lenght) * int(height)
	return area
def area_of_circle(rad):
	area = 3.14 * (int(rad) * int(rad))
	return area

def area_of_triangle(side):
	area = ((3)/4) * (int(side) * int(side))
	return area

while(True):
	print("Do you want to calculcate: ")
	print("1. Area of a rectangle.")
	print("2. Area of a circle.")
	print("3. Area of a triangle")
	print("0. Exit")
	user_choice = input("Enter choice: ")
	
	
	if user_choice == "1":
		lenght = input("What is the lenght of the rectangle. ")
		height = input("What is the height of the rectangle. ")
		print ("The area is " + str(area_of_rectangle(lenght,height)))
		
	if user_choice == "2":
		rad = input("What is the radius? ")
		print ("The area is " + str(area_of_circle(rad)))
	
	if user_choice == "3":
			side = input("What is one of the sides? ")
			print ("The area is " + str(area_of_triangle(side)))
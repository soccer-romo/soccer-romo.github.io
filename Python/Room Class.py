#Room Class

#Create a board with 3 rows and 3 columns
#Create start room
#Define each room separate from each other
#Name each room (1A,1B,1C, 2A,2B,etc.)
#Set up where each gate is
#Test if the wall has a door/needs key to unlock
#Display map of where you are in the rooms.
#Have the exit from the boss room be the win condition
#Win message
#Check if something is in the room

#My pusedocode)
#Use numbers by adding and subtracting to move across the board


"""Arron Burris, Alex Nguyen, David Niculcea, Tim Routen"""

rows = ["1","2","3"]
columns = ["A","B","C"]
locked = False
opened = True 
#start point
x = 2
y = 1

class Board():
	def section(rows, columns):
		print("___________________")
		print("|(" + rows[0]+","+columns[0]+")|(" +rows[0]+","+columns[1]+")|(" + rows[0]+","+columns[2]+")|")
		print("-------------------")
		print("|(" + rows[1]+","+columns[0]+")|(" +rows[1]+","+columns[1]+")|(" + rows[1]+","+columns[2]+")|")
		print("-------------------")
		print("|(" + rows[2]+","+columns[0]+")|(" +rows[2]+","+columns[1]+")|(" + rows[2]+","+columns[2]+")|")
		print("-------------------")
	section(rows, columns)

class Movement():

	def moveUp(rows,columns,x,y):
		x -=1
		y = y
		row = rows[x]
		column = columns[y]
		return x,y

	def movedown(rows,columns,x,y):
		x += 1
		y = y
		row = rows[x]
		column = columns[y]
		return x,y

	def moveleft(rows,columns,x,y):
		x = x
		y += 1
		row = rows[x]
		column = columns[y]
		return x,y

	def moveright(rows,columns,x,y):
		x = x
		y -= 1
		row = rows[x]
		column = columns[y]
		return x,y
		
	def showPosition(rows,columns,x,y):
		x = x
		y = y
		row = rows[x]
		column = columns[y]
		print(row + ","+ column)
		return x,y
		
	def movement(x,y):
		userMovement = input("")
		if (userMovement == "w"):
			x,y = Movement.moveUp(rows, columns, x, y)
		elif(userMovement == "s"):
			x,y = Movement.movedown(rows,columns,x,y)
		elif (userMovement == "a"):
			x,y = Movement.moveright(rows,columns,x,y)
		elif (userMovement == "d"):
			x,y = Movement.moveleft(rows,columns,x,y)
		return x,y
	
	def borders(x,y):
		x = x
		y = y
		if (x >= 3):
			x -= 1
			print("You've run into a wall.")
		elif (x <= -1):
			x += 1
			print("You've run into a wall.")
		elif (y <= -1):
			y += 1
			print("You've run into a wall.")
		elif (y >= 3):
			y -= 1
			print("You've run into a wall.")
		return x,y
	

def Room(rows, columns, x, y):
	x,y = Movement.showPosition(rows, columns, x, y)
	x,y = Movement.movement(x,y)		
	x,y = Movement.borders(x,y)
	return x,y


userExit = "yes"
print("You start out at (3,B). Good Luck! Use the w,a,s,d to guide yourself.")
while (userExit == "yes"):
	try:
		x,y = Room(rows, columns, x, y)
	except IndexError as e:
		print("You've run into a wall.")
	
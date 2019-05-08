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
import sys

rows = ["1","2","3"]
columns = ["A","B","C"]
unlocked = True
door = False
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
		
	def locked(doorPos, unlocked, x,y):
		x=x
		y=y
		if (x == 0 and y == 0 and doorPos != unlocked):
			x = 2
			y = 1
			print("Can't Enter. Please find key. You're now at the beginnning.")
		if (x == 0 and y == 0 and doorPos == unlocked):
			x = 0
			y = 1
		return x,y
	
	def key(door, unlocked, x, y):
		door = door
		if(x == 2 and y == 2):
			door = True
			print("GoodJob you've found the key!")
		return door
			
	def Exit(doorpos , unlocked, x,y):
		x = x
		y = y
		if (x == 0 and y == 1):
			print("You've won! Congrats!")
			sys.exit()
		return x,y
			
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
	


class Enemy():
	def enemySpot(door, unlocked,x,y):
		x = x
		y = y
		if (x == 0 and y == 0 and door == unlocked):
			print("enemy")
		return x,y
			

class Room():
	def spotInRoom(rows, columns, x, y):
		x,y = Movement.showPosition(rows, columns, x, y)
		x,y = Board.borders(x,y)
		doorPos = Board.key(door, unlocked, x, y)
		x,y = Board.locked(doorPos, unlocked, x, y)
		x,y = Movement.movement(x,y)		
		x,y = Enemy.enemySpot(door,unlocked,x, y)
		x,y = Board.Exit(doorPos, unlocked, x, y)
		return x,y




userExit = "yes"
print("You start out at (3,B). Good Luck! Use the w,a,s,d to guide yourself.")
while (userExit == "yes"):
	try:
		x,y = Room.spotInRoom(rows, columns, x, y)
		
	except IndexError as e:
		print("You've run into a wall.")
		
#use keys to set room as locked instead of creating walls. Just easier. [(x = ?) (y = ?) = set spots]
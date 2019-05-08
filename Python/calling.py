import sys
import Room_Class

rows = ["1","2","3"]
columns = ["A","B","C"]
unlocked = True
door = False
#start point
x = 2
y = 1


userExit = "yes"
print("You start out at (3,B). Good Luck! Use the w,a,s,d to guide yourself.")

while (userExit == "yes"):
	try:
		x,y = Room.spotInRoom(rows, columns, x, y)
	except IndexError as e:
		print("You've run into a wall.")
		
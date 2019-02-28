potato = 0


for i in range(8):
	potato = i + 1
	if (potato == 1 or potato == 2 or potato == 3 or potato == 5 or potato == 6 or potato == 7):
		print(str(potato) + " potato")
	elif ( potato == 4):
		print("four")
	elif (potato == 8):
		print("More:")
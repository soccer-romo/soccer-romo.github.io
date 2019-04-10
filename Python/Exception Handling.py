# Exeception Handling

num = 1

try:
	print("Number: " + str(num))
except TypeError as e:
	print("types do not match")
	print(e)
except ValueError as e:
	print("Some value error")
else:
	print("all is well")
	
try:
	f = open("I_don't_exist", "r")
except IOError as e:
	print("The file does not exist")
	print(e)
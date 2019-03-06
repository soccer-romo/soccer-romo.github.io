#Write a program that counts for the user. Let the user enter the starting number, the ending number, and the amount by which to count.
x = 0 
y = 0
interval = 0
print("This program will be used to count for you and the interval you want to use. ")
x = int(input("Please enter the beginning number you want to use: "))
y = int(input("Please enter the last number you want to use: "))

interval = int(input("At what interval do you want to count by: "))

for i in range(x,y,interval):
	print ("count " + str(i))
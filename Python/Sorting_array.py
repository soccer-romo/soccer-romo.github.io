# reference vs value
#
#name = "Bill "
#
#name = name.upper()
#
#print(name * 3)

#sorting

array_a = [2,3,1]

print(sorted(array_a))

print(array_a)

array_a.sort()

print(array_a)

array_a.sort(reverse=True)

print(array_a)

#tuples

array_b = ("blue","green","red")

print(sorted(array_b))

array_c = {1:["John"],2:["Paul"],3:["George"],4:["Rango"]}

print(sorted(array_c,reverse=True))

if (array_b.index("green")):
	print("Found!")

if (array_a.index(2)):
	print("found 2")
	
	
	
if "green" in array_b:
	print ("Phound 3")

for color in array_b:
	if color == "green":
		print ("found 4")
		break
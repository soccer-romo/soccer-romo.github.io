#list

colors = ["red","green","blue","blue","blue"]
#print(colors[0])
this_color = colors[0]
print(this_color)

colors.append("yellow")
print(colors)

colors.pop(1)
print(colors)

colors.remove(colors[1])

print(colors)

count_blue = colors.count("blue")
print(count_blue)

color_count = len(colors)
print(color_count)

colors.insert(2,"grey")

print(colors)

colors.reverse()
print (colors)

for color in colors:
	if (color == "grey"):
		continue
	print(color)	
		
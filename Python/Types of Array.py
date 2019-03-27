#array

#tuple

import random
colors = ("red","green","blue")

#print(colors[random.randint(0,2)])


for color in colors:
	print(color)
print("_____________________________________")
#list

colors = ["red","green","blue"]

colors[2] = "grey"

print(colors)

print("_____________________________________")
#nested list
#scores = [("moe",1000),("curely",1200),("larry",1500)]

scores = [["moe",1000],["curely",1200],["larry",1500]]
print(scores[2][0])
scores [0][1] = 1300
print(scores)
print("_____________________________________")
#dictionary

score = {"moe":[1000, "springfield", "north"],"curley":[1200, "springfield", "south"],"larry":[1500, "springfield", "north"]}

#print(score["curley"])

for k,v in score.items():
	print(k,v[0],v[1])
print("_____________________________________")
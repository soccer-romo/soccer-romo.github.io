#Write a program that flips a coin 100 times and then tells you the number of heads and tails.
#psudocode
#first import random
#set flip range from 1-2
#declare head and tail and total
#have it flip 100 times
#if head add it to total times it was head. Same for tails
#also add for total count

import random

head_count = 0
tail_count = 0
total_flip = 0

while (total_flip <= 99):
	flip = random.randrange(1,3)
	if (flip == 1):
		head_count += 1
		total_flip += 1
	elif (flip == 2):
		tail_count += 1
		total_flip += 1

print("Head Count: " + str(head_count) + " flips")	
print("Tail Count: " + str(tail_count) + " flips")

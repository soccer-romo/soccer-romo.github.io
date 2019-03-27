# Create a program that prints a list of words in random order. 
#The program should print all the words and not repeat any.
import random
random_word = random.randint(0,8)
list_of_words = ["Computer","PC","Monitor","Keyboard","Mouse","Speaker","Mic","Headphones","Laptop"]

random.shuffle(list_of_words)

print(list_of_words)
	


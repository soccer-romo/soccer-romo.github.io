def ask_question(ran_num):
	"""asking the question"""
	ran_num = ran_num
	questions = ["An array is composed of? ","The positions of an element is called? ","Arrays of the same size with the subscript related? ","When the value of an element depends on two factors instead of one? "]
	question = questions[ran_num]
	print("Question: " + question)
	return question

def answer(ran_num):
	"""having an answer"""
	ran_num = ran_num
	answers = ["a","b","c","d"]
	answer = answers[ran_num]
#	print (answer)
	return answer

def options():
	options = {"A)":["Elements"],"B)":["Subscript"],"C)":["Parallel Arrays"],"D)":["Two-Dimensional Array"]}
	for l,a in options.items():
		print(l,a[0])

def matching(question, answer):
	question = question
	answer = answer
	question = answer
	return question

def users_repsonse():
	user_answer = input("Type in your answer by letter: ").lower()
	return user_answer

user_exit = "yes"
import random

while (user_exit == "yes" or user_exit == "y"):		
	ran_num = random.randint(0,3)
	question = ask_question(ran_num)
	answer = answer(ran_num)
	options = options()
	answer = matching(question, answer)
	user_answer = users_repsonse()
	if (user_answer == answer):
		print("Good Job!")
		break
	while (user_answer != answer):
		user_answer = input("Try again: ")
		print(options)
		if (user_answer == answer):
			print("Good Job!")
			break
	user_exit = input("Do you still want to play? Type in yes or no: ").lower()
	if (user_exit != "yes" and user_exit != "y"):
		print("\n\nThank you for playing!")
		break


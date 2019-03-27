# More Functions and other bits and bobs:^)
"""
def myFuntion(parameters, go, here = "default"):
	"This is a docstring"
	print("do stuff")

def myFunction2(parameters, go, here):
	"This is a docstring"
	print("do stuff")

myFuntion2 (arguments, go, here) #positional

myFuntion(arguments, go) #uses default
myFuntion(arguments, go, here) #overrides
myFuntion(arugments = "test", go = "test2", here = "test 3") #named
"""


'''
var1 = None #other progamming languages null = None
var2 = ""
var3 = 0

var2 = input("enter something: ")

if var2 != "":
 print("do something")

if (var1):
	print("do another thing")
	'''

def printBandNames (names):
	for name in names:
		print (name)
		
		
bandMemembers = ["John", "Paul","Ruben", "Rambo"]

printBandNames(names = bandMemembers)
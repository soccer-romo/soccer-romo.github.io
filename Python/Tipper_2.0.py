bill_total = 0 
tip_percent = 0

bill_total = float(input("How much was your bill today? $"))

tip_percent= int(input("How much would you like to tip today 15% or 20%? "))

tip_percent = tip_percent * .01

bill_total = bill_total * tip_percent + bill_total

print("Your total plus tip will be: $" + str(bill_total))

input("\n\nPress the enter key to exit")

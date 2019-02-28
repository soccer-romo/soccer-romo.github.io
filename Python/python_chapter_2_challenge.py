#tipper program for class
restarant_bill_total = 0
tip_15 = .15
tip_20 = .20
tip_0 = 0
restarant_bill_total = int(input("How much is your restarant bill today? $"))
print ("Okay so your bill is $" + str(restarant_bill_total))

tip_0 = int(input("How much would you like to tip today 15% or 20%? "))
if tip_0:  15
tip_0 = tip_15
if tip_0: 20
tip_0= tip_20

restarant_bill_total = float(restarant_bill_total * tip_0) + restarant_bill_total
print ("This is your bill total plus tax: $" + str(float(restarant_bill_total))+ " Thank you!")

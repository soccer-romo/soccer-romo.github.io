car_base_price = 0
tax = 0
tax_rate = .0778
license = .01
dealer_prep = 150
destination_charge = 255 
car_base_price = int(input("What is the base price of the car that you're looking at today? $"))

print("Only $" + str(car_base_price) + "! That's not too bad. Well it looks like the car's total comes to: $" + str(car_base_price * tax_rate  +  car_base_price * license  + dealer_prep + destination_charge + car_base_price) + ". That's including the tax (7.78%), the license (1%), the dealer's prep charge ($150), and the destination charge ($255). Enjoy!")

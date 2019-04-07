#car class examples

class Car:
	def __init__(self,car_color,car_type,engine_size):
		self.car_color = car_color
		self.car_type = car_type
		self.engine_size = engine_size
		
	def revEngine(self):
		if (self.engine_size == "V6"):
			return "zoom zoom"
		elif (self.engine_size == "V8"):
			return "vroom vroom"
		
		
c1 = Car("blue","coupe","V6")

print(c1.car_color)

print(c1.revEngine())

c2 = Car("red", "truck", "V8")

print(c2.car_color)
print(c1.revEngine())
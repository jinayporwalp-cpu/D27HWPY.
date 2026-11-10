class Vehical:
	def __init__(self,brand,max_speed):
		self.brand = brand
		self.max_speed = max_speed

	def show_details(self):
		print("brand",self.brand)
		print("max speed",self.max_speed)

class Car(Vehical):
	def __init__(self, brand, max_speed,model,seats):
		self.model1 = model
		self.seats = seats
		super().__init__(brand,max_speed)

	def show_details(self):
		print("model ",self.model1)
		print("seats",self.seats)

	def fuel_type(self,fuel):
		print(self.model1,"uses",fuel)

my_car = Car("CITY RIDER ",5,"honda",180)

my_car.show_details()
my_car.fuel_type("petrol")

print("is car a subclass of vehical",
issubclass(Car,Vehical))
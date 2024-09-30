#10. Multiple Inheritance
# Problem: Create two classes Battery and Engine, and let the ElectricCar class inherit from both, demonstrating multiple inheritance.

# => Class- Car ---
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model

    def full_name(self):
        return f"A Car of {self.brand} brand and its model is {self.__model}"

# => Instant of Class Car ---

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size 

    def full_name(self):
        car_details = super().full_name()
        return f"{car_details} and the battery size is {self.battery_size}"



my_car = Car('Tata', 'Safari')

my_tesla =  ElectricCar('Tesla', 'Model-S', '50kWh')


#Create two class

class Battery():
    def batter_info(self):
        return 'This is battery'

class Engine():
    def engine_info(self):
        return 'This is engine'


class ElectricCarTwo(Battery, Engine, Car):
    pass

my_new_tesla = ElectricCarTwo('Tesla', 'Model S')

print(my_new_tesla.brand)
print(my_new_tesla.engine_info())
print(my_new_tesla.batter_info())

#NOTE: - yes here multiple inheritance possible in python 
# we can simple access them through object
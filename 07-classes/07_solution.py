#7. Static Method
# Problem: Add a static method to the Car class that returns a general description of a car.

#NOTE: - A method that available in class (Car) but not in the instance of the class (object - my_car/my_car_two can not access) i.e. Static Method.
# - When we write using only Car.()

#NOTE: 
#   - @staticmethod - is a decorates
#   - @staticmethod - when it is use do not need the (self) linking as      parameter
#   - @staticmethod - objects can't access only parent class access



# => Class- Car ---
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"A Car of {self.brand} brand and its model is {self.model}"
    
#- Static method that only Car. use not its objects

    @staticmethod #- It is a Decorates NOTE
    def general_desc():
        return "Cars means transports"

# => Instant of Class Car ---

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size 

    def full_name(self):
        car_details = super().full_name()
        return f"{car_details} and the battery size is {self.battery_size}"
    


my_car = Car('Tata', 'Safari')
my_car_two = Car('Tata', 'Nexon')
Car('Honda', 'CIty') #- do not need to store in variable that reference

my_tesla =  ElectricCar('Tesla', 'Model-S', '50kWh')


# print(my_car.general_desc()) 
print(Car.general_desc())


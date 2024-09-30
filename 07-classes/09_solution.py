#9. Class Inheritance and isinstance() Function
# Problem: Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar.

#NOTE: - isinstance() = it is a method gives boolen value (T/F) to check the object is instance of a class or not 
# - is = Boolen value IMP

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


#NOTE: - isinstance() = isinstance(object name, class name)

print(isinstance(my_tesla, Car)) #True
print(isinstance(my_tesla, ElectricCar)) #True

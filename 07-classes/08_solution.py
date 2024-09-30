#8. Property Decorators
# Problem: Use a property decorator in the Car class to make the model attribute read-only.

#IMP:- When we use @property decorator it helps to hide the function that limited people can access when they access need the methods to acces
#   - It helps when the constructor set you can not override that -  NOTE
#   - [ __ ] = it also hide and privaties the variables

# => Class- Car ---
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.__model = model

    def full_name(self):
        return f"A Car of {self.brand} brand and its model is {self.__model}"
    #NOTE: - @proerty method -  decorator is helps to access the function as a property
    @property
    def model(self):
        return self.__model

# => Instant of Class Car ---

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size 

    def full_name(self):
        car_details = super().full_name()
        return f"{car_details} and the battery size is {self.battery_size}"



my_car = Car('Tata', 'Safari')
# my_car.model = 'City'

print(my_car.model)


my_tesla =  ElectricCar('Tesla', 'Model-S', '50kWh')




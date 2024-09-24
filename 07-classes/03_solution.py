#3. Inheritance
# Problem: Create an ElectricCar class that inherits from the Car class and has an additional attribute battery_size.

#- >  IMP -- INHERITANCE -- IMP
#- It allows you to inherits properties and methods from another class IMP

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"A Car of {self.brand} brand and its model is {self.model}"

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size #- This is the child parameter need to write

#NOTE: - override the full name and add battery info into that
    def full_name(self):
        car_details = super().full_name() # Get parent [Car] full name method 
        return f"{car_details} and the battery size is {self.battery_size}"

my_tesla =  ElectricCar('Tesla', 'Model-S', '50kWh')
print(my_tesla.brand)
print(my_tesla.battery_size)
print(my_tesla.full_name())

# my_tesla =  ElectricCar(brand, model, battery_size) - model/brand inherit from parent class [Car] through super() keyword NOTE:

#- super()-keyword use for access propertis of parent class insilde child class NOTE:



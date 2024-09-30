#5. Polymorphism
# Problem: Demonstrate polymorphism by defining a method fuel_type in both Car and ElectricCar classes, but with different behaviors.

#NOTE: - Somthing that can take multiple forms (variantes) that is calles polymorphism

# => Class- Car ---
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def full_name(self):
        return f"A Car of {self.brand} brand and its model is {self.model}"

# Polymorphism - TODO
    def fuel_type(self):
        return f"{self.brand} Car have Petrol or Diesel fuel"



# => Instant of Class Car ---

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size 

    def full_name(self):
        car_details = super().full_name()
        return f"{car_details} and the battery size is {self.battery_size}"
    
# Polymorphism - TODO
    def fuel_type(self):
        return f"{self.brand} Car have electric charge"

my_car = Car('Tata', 'Safari')
my_tesla =  ElectricCar('Tesla', 'Model-S', '50kWh')


print(my_car.fuel_type()) #- Car object
print(my_tesla.fuel_type()) #- ElectricCar object

#NOTE:- Two different class object using same method to print different value that in POLYMORPHISM.
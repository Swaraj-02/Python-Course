#6. Class Variables
# Problem: Add a class variable to Car that keeps track of the number of cars created.

# => Class- Car ---
class Car:

    total_car = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        # self.total_car += 1 #- mostly use
        Car.total_car += 1 #- another approch

    def full_name(self):
        return f"A Car of {self.brand} brand and its model is {self.model}"

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

print(Car.total_car) # 4 - anonimous, my_car, my_car_two and my_tesla [inherit]

#NOTE:- when object is created that time constructer is called 

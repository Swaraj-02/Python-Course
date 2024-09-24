#2. Class Method and Self
# Problem: Add a method to the Car class that displays the full name of the car (brand and model).

# __init__ it is the constructor function IMP:

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

        # Normal
        # car_name = brand + model
        # print(car_name)

    #functionality
    #use the connection line (self) as a 1st parameter if not it will not conected to the above variable IMP:
    def full_name(self):
        return f"Full Name:- {self.brand} {self.model}"
    

my_car = Car('Tata', 'Safari')
print(my_car.brand)
print(my_car.model)
print(my_car.full_name())  # full_name() is a function




#1. Basic Class and Object
# Problem: Create a Car class with attributes like brand and model. Then create an instance of this class.

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    # def hello():
    #     print('Hello Car Object')

my_car = Car("Tata", "Safari")
print(my_car.brand)
print(my_car.model)


my_new_car = Car("Honda", "City")
print(my_new_car.brand)
print(my_new_car.model)

#__init__ => it the constructor function inside class IMP:
# self => it is the connection that connect constructor and class without this 1st parameter connection will not build IMP:

#delete the my_new_car object using del keyword


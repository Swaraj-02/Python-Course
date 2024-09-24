#4. Encapsulation
# Problem: Modify the Car class to encapsulate the brand attribute, making it private, and provide a getter method for it.

# NOTE - To privaties the properties of any class and when a another class need the permission to access that, i.e called Encapsulation.
# IMP - in python [ ' __ ' ] double underscore is the syntax that is known as for encapsulation

class Car:
    def __init__(self, brand, model):
        self.__brand = brand
        self.model = model

    #NOTE: getter() - (brand) to private - inside call we can use but when object create it not accesable
    def get_brand(self):
        return self.__brands
    
    #IMP- Setter () - set the new attributes new_brand_name  of brand
    def set_brand(self, new_brand_name):
        self.__brand = new_brand_name + ' !'


    def full_name(self):
        return f"A Car of {self.__brand} brand and its model is {self.model}"

class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size 

my_tesla =  ElectricCar('Tesla', 'Model-S', '50kWh')

# print(my_tesla.__brand) # Tesla - Not running due to brand is private now

#NOTE:- get_brand() is method need to call when you want access the brand 
# print(my_tesla.get_brand()) # Tesla !
print(my_tesla.set_brand('Tata')) # Tata

print(my_tesla.full_name()) #- A Car of Tesla brand and its model is Model-S
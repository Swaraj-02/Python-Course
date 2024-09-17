#8. Function with **kwargs
# Problem: Create a function that accepts any number of keyword arguments and prints them in the format key: value.

def print_kwargs(**kwargs):
    for key, value in kwargs.items(): # loop on every item
        print(f"{key}: {value}")

print_kwargs(name="shaktiman")
print_kwargs(name="swaraj", age=15, behavior="good")

#we can pass the as many key, value pair value like using **kwargs IMP
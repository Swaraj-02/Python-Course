#5. Default Parameter Value
# Problem: Write a function that greets a user. If no name is provided, it should greet with a default name.

#-My Approch

def greet_user():
    name = str(input('Enter a name:- '))
    if name:
        print(f"{name} Welcome!")
    if not name:
        print('Welcome Default!')

greet_user() 

#- Instructor Approch
# we can define a default value to parameter (parameter is required field -IMP) if the user did not write any parameter to function then it print the default one. 

def greet(name = "User"):
    return "Hello " + name + " !"

print(greet("Raja")) # Giving value to parameter - Hello Raja !
print(greet()) # Not giving value to parameter - Hello User !
    
#3. Polymorphism in Functions
# Problem: Write a function multiply that multiplies two numbers, but can also accept and multiply strings.

# My 1st approch where i did not understand last line of question
def multiply (numOne,numTwo,stringval):
    return  numOne * numTwo * stringval


print(multiply(2,4,'swaraj'))

print('-----------------------------------')

#instructor approch-

def multiply_all(valOne,valTwo):
    return valOne * valTwo

print(multiply_all(5,5))
print(multiply_all('s',5))
print(multiply_all(5,'s'))
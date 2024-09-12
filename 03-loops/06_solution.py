#6. Factorial Calculator
# Problem: Compute the factorial of a number using a while loop.

# ex- factorial of 4 = 4*3*2*1

number = int(input('Enter A Number:- '))
factorial = 1

num = number

while number > 0:
    factorial = factorial * number
    number = number -1

print(f"Factorial of {num} is:- {factorial}")
    
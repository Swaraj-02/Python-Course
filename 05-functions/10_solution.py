#10. Recursive Function
# Problem: Create a recursive function to calculate the factorial of a number.

#- Recursive Function -> You called the function again and again when you inside the function IMP

#- When we have problem like recursion then thisnk about exit strategy 

num = int(input('Enter a number:- '))

def factorial(n):
    if n == 0:  
        # recursive function exit strategy when the factorial value of number = n is o then it gives 1 (0 factorial = 1)
        return 1
    else:
        return n * factorial(n - 1) # here inside function a recursive function called
    
print(factorial(num)) #- 5 = 120
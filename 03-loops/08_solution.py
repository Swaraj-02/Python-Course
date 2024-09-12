#8. Prime Number Checker
# Problem: Check if a number is prime.

#Def- A number is greater than 1 and divided by itself IMP

number = int(input('Enter a number:- '))

is_prime = True # assume entered number is Prime if prime then print True IMP

if number > 1: #number is greater than 1
    for i in range(2, number): 
        if (number % i) == 0: #check is between 1 to n number is reminder get 0 then its false and break the loop IMP
            is_prime = False
            break

print(f"The {number} is a Prime Number:- {is_prime}")
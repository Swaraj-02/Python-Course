# 1. Basic Function Syntax
# Problem: Write a function to calculate and return the square of a number.

# ex-1
def square(num):
    return num ** 2
# if we use return then when ever we call funtion and give value it gives functionality return 

print(square(4)) #16

result = square(4) #16 stored in result variable
print(result) # 16

print('-------------------------------------')
# ex-2 
# if we not using return key word then the function value not stored in any variable it excute when we call the function(one time)
def square(num):
    print(num ** 2)

square(4) # 16

result = square(4) 
print(result) #none



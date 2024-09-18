#- scopes

x = 99

def funcOne():
    x = 88
    print(x)

print(x) # - 99 - Golbal variable IMP
funcOne() # - 88 - variable inside the funcOne scope IMP

def funcTwo():
    global x 
    x = 77
    print(x) 

funcTwo() 
#- now the value is x = 77, coz we override the value using global keyword inside the scope IMP

#- Closures
#-> when the function called inside the function another function defination along with variable will go and stored into memory reference that is callled clousers IMP:

def f1(num):
    def f2(x):
        return x ** num
    return f2 # f2() - function // f2 - reference

f3 = f1(2) # num = 2
print(f3(3)) # x = 3

# Answer = 27
# def f1(2):
#     def f2(3):
#         return 3 ** 2
#     return f2  
# = 27 answer
# 7. Function with *args
# Problem: Write a function that takes variable number of arguments and returns their sum.

# if we want to sum multiple arguments when we print then we use *args for it = * - for multiple arguments IMP

def sum_all(*args):
    return sum(args)  # id return keyword not use it gives- none (output)
    # sum() is a in build method in python to sum all variables IMP

print(sum_all(1,2,3))

#- Investication Study 

def sumAll(*args):
    print(args) # (1,2,3) - in tuple formats () paranthis
    for i in args:
        print(i * 2) # 2, 4, 6

sumAll(1,2,3)

#- we can do sum,multiplication all using *args in python
#- * - it is mandotory / args is optional but recommended IMP
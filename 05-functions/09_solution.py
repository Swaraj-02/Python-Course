#9. Generator Function with yield
# Problem: Write a generator function that yields even numbers up to a specified limit.


# my Approch -
num_upto = int(input('Enter a number:- ')) #- 10

def even_generator (limit):
    for i in  range(2, limit + 1, 2): # 2 = skip the value upto 2 the write again skip the value upto 2 then write
    #range('start value', 'range upto', 'except value') IMP:
        if i % 2 == 0:
            print(i)

even_generator(num_upto) #- 2, 4, 6, 8, 10


print("---------------------------------------")
# Instructor Approch using Yeild - 

#=> yeild IMP
#       - it stored the value in memory and return it
#       - this make function generator insted only returning values at once it returns one value at a time when asked (during iteration) 

def Generator(limit):
    for i in range(2,limit + 1, 2):
        yield i

for num in Generator(10):
    print(num) #- 2, 4, 6, 8, 10
#4. Function Returning Multiple Values
# Problem: Create a function that returns both the area and circumference of a circle given its radius.

# Area = pie * R ** 2 (pieXr_square)
# Circumference = 2pieR (2 X pie X Radius)

radius = int(input('Enter the Radius of Circle:- '))

def circle():
    area = 3.14 * radius ** 2
    circumference = 2 * 3.14 * radius
    return f"Circle Area - {area},\nCircle Circumference:- {circumference}"

print(circle())

print('------Approch-2 using parameter and math.pi ------------')
#ex-2 using parameter and importing pie from math (Approch -2)
import math

def circle(Radius):
    area = math.pi * Radius ** 2
    circumference = 2 * math.pi * Radius
    # return area, circumference - #IMP - getting 50.26548245743669 , 25.132741228718345 this type value so we use floor for 2 digit value
    return math.floor(area), math.floor(circumference)


Area,Circumference = circle(4) # also you can destructure value like that

print("Area:- ", Area, "\n","Circumference:- ", Circumference)
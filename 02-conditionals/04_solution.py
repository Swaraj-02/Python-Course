#4.-  Fruit Ripeness Checker
# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

#- Here i did it it on my own to get input and print i do not use the example of  (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

fruit = str(input("Enter a fruit name:- "))
color = str(input("Enter the color of the fruit:- "))

# print(type(fruit))
# print(type(color))

if fruit:
    if color == 'Green':
        print('Unripe')
    elif color == 'Yellow':
        print('Ripe')
    elif color == "Brown":
        print('Overripe')
    else: 
        print('I do not know about this fruits')



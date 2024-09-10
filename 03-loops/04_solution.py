#4. Reverse a String
# Problem: Reverse a string using a loop.

char = str(input('Enter a string to reverse:- '))
reversed_char = ""

#Here given to do with using loop- IMP:
for i in char:
    reversed_char = i + reversed_char  # change the string using is placed IMP

print(f"Before Reversed - {char} \nAfter Reversed - {reversed_char}")
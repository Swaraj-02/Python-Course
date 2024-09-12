#5. Find the First Non-Repeated Character
# Problem: Given a string, find the first non-repeated character.

input_char = str(input('Enter a String:- '))

for char in input_char:
    print(char)
    if input_char.count(char) == 1:
        print('Charecter is:-',char)
        break # to break the where we get out output 
    # here we need (first non-repeated character) so use break keyword to not go on loops trough all charecter we need only first non repeated value IMP

    
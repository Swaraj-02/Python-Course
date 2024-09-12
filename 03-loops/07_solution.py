#7. Validate Input
# Problem: Keep asking the user for input until they enter a number between 1 and 10.

# here need infinite loop until the user not enter number between 1-10 so we use While loop IMP


while True:
    user_input = int(input('Enter A Number:- '))
    if user_input >= 1 and user_input <= 10: # if 1<= user_input <= 10 (Alternative) IMP
        print('Thanks')
        break
    else:
        print('User Input Is Invalid, Try Agian')
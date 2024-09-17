#6. Lambda Function
# Problem: Create a lambda function to compute the cube of a number.

# Function that does not have name (Lambda / Annonimos function)- IMP:
#- Used for instat use in one time in a program
#- It is mostly used in frameworks 

# Lambda Function 

cube = lambda x:x **3 #lamda - keyword , before colon (:) x is parameter IMP
print(cube(4)) #-> 64

# Regular Function

def cube_of_num (num):
    return num ** 3
print(cube_of_num(4)) #-> 64
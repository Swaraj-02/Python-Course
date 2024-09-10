#10. Pet Food Recommendation
#Problem: Recommend a type of pet food based on the pet's species and age. (e.g., Dog: <2 years - Puppy food, Cat: >5 years - Senior cat food).

pet_type = str(input("Enter your Pet's type:- ")).capitalize()
pet_age = int(input(f"Enter your {pet_type} age:- "))

if pet_type == 'Dog':
    if pet_age < 2:
        print("Puppys Food")
    else:
        print("Adults Food")
elif pet_type == 'Cat':
    if pet_age >= 5:
        print("Senior Cat Food")
    else:
        print("Junior Cat Food")
else:
    print("I don't have the species details")
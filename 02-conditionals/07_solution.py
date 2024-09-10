#7- Coffee Customization
# Problem: Customize a coffee order: "Small", "Medium", or "Large" with an option for "Extra shot" of espresso.

order_size = str(input("Enter your order size (Small/Medium/Large):- "))
extra_short = input("You want extra short or not ? (Yes/No):- ")

if extra_short == "Yes":
    coffee = order_size + " Coffee with extra shorts"
else:
    coffee = order_size + " Coffee with no extra shorts"

print(coffee)

# print(type(extra_short)) - Boolean = True / false 
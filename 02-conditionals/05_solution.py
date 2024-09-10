#5- Weather Activity Suggestion
# Problem: Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).

weather = str(input('Enter the Weather (Sunny/Rainy/Snowy):- '))

if weather == 'Sunny':
    activity = "Go for a walk"
elif weather == 'Rainy':
    activity = "Read a book"
elif weather == 'Snowy':
    activity = "Build a snowman"
else:
    activity = "I don't have the weather information"

print("Based on weather you can do this -",activity)

# print(type(activity)) - String (type)
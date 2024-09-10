# 2. Movie Ticket Pricing -
# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.
import datetime

#we can use datetime module to extract exact day and use it in our program
# date = datetime.datetime.now()
# print(date.strftime("%A"))



print('Movie Ticket ($2 Discount on Wednesday)')


age = int(input('Enter the age:- '))
day = str(input('Enter the day:- '))

price = 12 if age >= 18 else 8 #- get the price according to age


if day.lower() == 'wednesday': #- check the day 
    price = price - 2  #- $2 discount on price in wednesday

if age < 18:
    print(f'Ticket price for Children - ${price}')
elif age >= 18:
    print(f'Ticket price for Adults - ${price}')


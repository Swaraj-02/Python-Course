# 9- Leap Year Checker
# Problem: Determine if a year is a leap year. (Leap years are divisible by 4, but not by 100 unless also divisible by 400).

year = int(input('Enter a Year to check Leap year or not:- '))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0): 
    #in this case parenthiis are IMP: ()
    print(year, 'is a Leap year')
else:
    print(year, 'is not a Leap year')
# 3.Grade Calculator - 
# Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

#- we can do this in both way using if-elif and matcch-case using 
#- before python 10.3 (use if-elif for such program) in python not concept of switch case after that update a alternative option match-case (alt of switch case) //IMP

#- if-elif //IMP

percentage = int(input('Enter your Percentage:- '))

if percentage >= 101:
    print('Please verify your percentage again')
    exit()

if percentage >= 90:
    grade = "A"
elif percentage >=80:
    grade = "B"
elif percentage >=70:
    grade = "C"
elif percentage >=60:
    grade = "D"
else:
    grade = "F"

print('Grade:- ',grade)

#- match-case //IMP

#we can not directly use Match-Case (expression - case score >= 90) coz case expect a patterns into it so -
                #-To include conditions, you should use a guard (if clause) after a pattern.or a { _ } place holder like that

score = int(input('Enter your score:- '))

if score >= 101:
    print('Please verify your score again')
    exit()

match score:
    case _ if score >= 90: # under score used for place holder 
        print('Grade : A')
    case _ if score >= 80:
        print('Grade : B')
    case _ if score >= 70:
        print('Grade : C')
    case _ if score >= 60:
        print('Grade : D')
    case _ :
        print('Fail')
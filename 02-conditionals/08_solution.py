#8- Password Strength Checker
#Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

password = str(input('Enter your Password:- '))

#optimization - stored in len() in a variable

password_len = len(password)

if password_len < 6:
    print('Weak')
elif password_len <= 10:
    print('Medium')
else:
    print('Strong')


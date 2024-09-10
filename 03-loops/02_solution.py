#2. Sum of Even Numbers
# Problem: Calculate the sum of even numbers up to a given number n.

given_num = int(input('Enter the number:- '))
sum_of_num = 0

for i in range(1, given_num + 1):
    if i % 2 == 0:
        sum_of_num += i

print(f"Sum of even number in {given_num} is = {sum_of_num}")



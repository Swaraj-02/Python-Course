#1. Counting Positive Numbers
# Problem: Given a list of numbers, count how many are positive.

# ```python
# numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
# ```

numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
positive_count_num = 0

for num in numbers:
    if num > 0:
        positive_count_num = positive_count_num + 1

print(positive_count_num)
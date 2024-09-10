#3. Multiplication Table Printer
# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

num = int(input('Enter the Number:- ')) # 5

for i in range(1, 11):
    if i == 5:
        continue # it check the 5 spot and detect that to skip and continue = here i == 5 (skip fifth[5] spot)
    print(f"{num} X {i} = {num * i}")



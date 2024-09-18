# 4. Given a list of numbers, find the maximum and minimum values.

#- Without using min() / max() in built method using python IMP

list_of_nums = [1,64,16,78,]

def find_mx_min(number):
    if len(number) == 0:
        return None, None
    
    max_value = number[0]
    min_value = number[0]

    for num in number[1:]: # [1:]-> slice method start from 1 and itrate from the end of the list IMP:
        if num > max_value:
            max_value = num
        if num < min_value:
            min_value = num

    return max_value, min_value

max_value, min_value = find_mx_min(list_of_nums)

print(f"Max Number:- {max_value} \nMin Number:- {min_value}")
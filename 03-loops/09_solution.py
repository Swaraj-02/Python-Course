#9. List Uniqueness Checker
# Problem: Check if all elements in a list are unique. If a duplicate is found, exit the loop and print the duplicate.

# ```python
# items = ["apple", "banana", "orange", "apple", "mango"]

items = ["apple", "banana", "orange", "apple", "mango"]

unique_item = set() # set() stroed unique value

for item in items:
    if item in unique_item: # check in the unique item the (item value is added before or not) if added then print the item and break the statement
        print("Duplicate: ", item) # apple
        break
    else:
        unique_item.add(item) 

print("Unique Item is :-",unique_item) # print the item untill the duplicate item found here- {'apple', 'banana', 'orange'}
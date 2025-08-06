# By Henok Girma
# week 2 python programming assignment for PLP africa fully funded software engineering scholarship program
# This script demonstrates basic list operations in Python.
# Step 1: Create an empty list
my_list = []

# Step 2: Append the elements 10, 20, 30, 40, it becomes [10, 20, 30, 40]
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# Step 3: Insert 15 at the second position (index 1), it becomes [10, 15, 20, 30, 40]
my_list.insert(1, 15)

# Step 4: Extend the list with [50, 60, 70], it becomes [10, 15, 20, 30, 40, 50, 60, 70]
my_list.extend([50, 60, 70])

# Step 5: Remove the last element, it becomes [10, 15, 20, 30, 40, 50, 60]
my_list.pop()

# Step 6: Sort the list in ascending order, it becomes [10, 15, 20, 30, 40, 50, 60]
my_list.sort()

# Step 7: Find and print the index of value 30, which should be 3
index_of_30 = my_list.index(30)
print("Index of 30:", index_of_30)

# Optional: Print the final list to see the result, it should be [10, 15, 20, 30, 40, 50, 60]
print("Final List:", my_list)


#Creating a list
my_list = [1, 2, 3, 4, 5]

# Using methods: append, extend, remove, reverse
my_list.append(6)  # Appending 6 to the list
print(my_list)

my_list.extend([7, 8, 9])  # Extending the list with another list
print(my_list)

my_list.remove(6)  # Removing the element 6 from the list
print(my_list)

my_list.reverse()  # Reversing the list
print(my_list)

# Arranging the list in ascending and descending order
my_list.sort()  # Ascending order
print(my_list)

my_list.sort(reverse=True)  # Descending order
print(my_list)


# Given list
List1 = [1, 2, 3, 4, ["python", "java", "c++", [10,20,30]], 5, 6, 7, ["apple", "banana", "orange"]]

# Getting "orange" and "python" from the list
word_orange = List1[-1][-1][-1]
word_python = List1[4][0]

# Repeating the list five times without using loops
repeated_list = [List1] * 5

print("Word 'orange':", word_orange)
print("Word 'python':", word_python)
print("Repeated list:", repeated_list)
      

      # Creating a list
original_list = [1, 2, 3, 4, 5]

# Copying the list using slice function
copied_list = original_list[:]

print("Original List:", original_list)
print("Copied List:", copied_list)
      
      # Creating a tuple
my_tuple = (1, 2, 3, 4, 5)

# Applying mathematical operations
sum_tuple = sum(my_tuple)  # Sum of all elements
max_tuple = max(my_tuple)  # Maximum value
min_tuple = min(my_tuple)  # Minimum value

print("Sum of tuple:", sum_tuple)
print("Maximum value of tuple:", max_tuple)
print("Minimum value of tuple:", min_tuple
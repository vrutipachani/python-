# 1. Reverse the given string
given_string = "Hello, World!"
reversed_string = given_string[::-1]

# 2. Replace some character of the string with another character
modified_string = given_string.replace('l', 'z')

# 3. Find whether the character in the given string or not
char_exists = 'o' in given_string

# 4. Create tuple, list, and set and convert them into different strings
my_tuple = (1, 2, 3)
my_list = [4, 5, 6]
my_set = {7, 8, 9}
tuple_string = str(my_tuple)
list_string = str(my_list)
set_string = str(my_set)

# 5. Convert all the string characters to upper and lower case and split it with different methods
upper_case = given_string.upper()
lower_case = given_string.lower()
split_method = given_string.split(',')
split_index = given_string.split(' ')[0]

# 6. Perform operations to the tuple and the list: find max, min, len, sum
max_tuple = max(my_tuple)
min_tuple = min(my_tuple)
len_tuple = len(my_tuple)
sum_tuple = sum(my_tuple)

max_list = max(my_list)
min_list = min(my_list)
len_list = len(my_list)
sum_list = sum(my_list)

# 7. Copy one list to another list without using the copy command
copied_list = my_list[:]

# 8. Perform operations on dictionary
student = {'name': 'John', 'age': 20, 'grade': 'A'}
age_of_student = student['age']
student['grade'] = 'B'
gender_present = 'gender' in student

# 9. Perform operations on sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1.union(set2)
intersection_set = set1.intersection(set2)
difference_set = set1.difference(set2)
subset_check = set1.issubset(set2)

# 10. Perform operations on dictionary of sets
subjects_dict = {'math': {'John', 'Alice'}, 'science': {'Bob', 'Alice'}}

subjects_dict['math'].add('Emma')
subjects_dict['science'].remove('Bob')

common_students = subjects_dict['math'].intersection(subjects_dict['science'])

# 11. Create two lists, one containing elements at even indices and the other containing elements at odd indices
original_list = [1, 2, 3, 4, 5, 6]
even_indices_list = original_list[::2]
odd_indices_list = original_list[1::2]

# 12. Use tuple packing and unpacking to swap the values of two variables without using a temporary variable
a, b = 1, 2
a, b = b, a

# 13. Check if a given list is a palindrome using slicing
palindrome_list = [1, 2, 3, 2, 1]
is_palindrome = palindrome_list == palindrome_list[::-1]

# 14. Concatenate two tuples without using the + operator
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
concatenated_tuple = tuple1._add_(tuple2)

print("Results:")
print("Reversed string:", reversed_string)
print("Modified string:", modified_string)
print("Character 'o' exists in given string:", char_exists)
print("Tuple as string:", tuple_string)
print("List as string:", list_string)
print("Set as string:", set_string)
print("Upper case:", upper_case)
print("Lower case:", lower_case)
print("Split method result:", split_method)
print("Split by index result:", split_index)
print("Max of tuple:", max_tuple)
print("Min of tuple:", min_tuple)
print("Length of tuple:", len_tuple)
print("Sum of tuple:", sum_tuple)
print("Max of list:", max_list)
print("Min of list:", min_list)
print("Length of list:", len_list)
print("Sum of list:", sum_list)
print("Copied list:", copied_list)
print("Age of student:", age_of_student)
print("Modified grade of student:", student['grade'])
print("Is 'gender' key present in student dictionary:", gender_present)
print("Union of sets:", union_set)
print("Intersection of sets:", intersection_set)
print("Difference of sets:", difference_set)
print("Is set1 a subset of set2:", subset_check)
print("Updated subjects dictionary:", subjects_dict)
print("Even indices list:", even_indices_list)
print("Odd indices list:", odd_indices_list)
print("Is the list a palindrome:", is_palindrome)
print("Concatenated tuple:", concatenated_tuple)
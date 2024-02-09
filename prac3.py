# String Operations
# Reverse a string
string = "hello"
reversed_string = string[::-1]
print("Reversed string:", reversed_string)

# Replace a string with another string
string = "hello world"
new_string = string.replace("world", "universe")
print("String after replacement:", new_string)

# Merge two strings
string1 = "hello"
string2 = " world"
merged_string = string1 + string2
print("Merged string:", merged_string)

# Find if a character is in a string without using loops
string = "hello"
character = 'e'
is_present = character in string
print(f"Character '{character}' is present in the string: {is_present}")

# Split a string into multiple words and characters
string = "hello world"
words = string.split()  # Split into words
characters = list(string)  # Split into characters
print("Words:", words)
print("Characters:", characters)

# Dictionaries Operations
# Create dictionaries
dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5, 'f': 6}

# Merge dictionaries into one
merged_dict = {**dict1, **dict2, **dict3}
print("Merged dictionary:", merged_dict)

# Apply "Update, Delete, Clear, popitem, pop, get, keys, and values" operations in a dictionary
my_dict = {'a': 1, 'b': 2, 'c': 3}

# Update
my_dict.update({'d': 4})

# Delete
del my_dict['a']

# Clear
my_dict.clear()

# Popitem
key, value = my_dict.popitem()

# Pop
value = my_dict.pop('b')

# Get
value = my_dict.get('c')

# Keys
keys = my_dict.keys()

# Values
values = my_dict.values()

print("Updated dictionary:", my_dict)
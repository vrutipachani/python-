 A) Function to determine grade based on SGPA
def get_grade(sgpa):
    if sgpa >= 9.0:
        return 'S'
    elif sgpa >= 8.0:
        return 'A'
    elif sgpa >= 7.0:
        return 'B'
    elif sgpa >= 6.0:
        return 'C'
    elif sgpa >= 5.0:
        return 'D'
    else:
        return 'F'

# B) Function to find maximum of three numbers
def find_max(num1, num2, num3):
    return max(num1, num2, num3)

# C) Function to count uppercase and lowercase letters in a string
def count_letters(string):
    uppercase_count = sum(1 for char in string if char.isupper())
    lowercase_count = sum(1 for char in string if char.islower())
    return uppercase_count, lowercase_count

# D) Function to find square of elements in a list using lambda function
square_list = lambda lst: [x**2 for x in lst]

# E) Function to print multiplication table
def multiplication_table(num):
    for i in range(1, 11):
        print(f"{num} x {i} = {num * i}")

# F) Function to create a list and calculate its sum using loop
def sum_of_list():
    values = input("Enter values separated by spaces: ").split()
    numbers = [float(val) for val in values]
    total_sum = sum(numbers)
    return total_sum

# G) Function using list comprehension to create lists of even and odd numbers, and numbers divisible by 5
even_numbers = [x for x in range(1, 51) if x % 2 == 0]
odd_numbers = [x for x in range(1, 51) if x % 2 != 0]
divisible_by_5 = [x for x in range(1, 101) if x % 5 == 0]

# Testing the functions
print("Grade:", get_grade(8.5))
print("Max number:", find_max(10, 20, 30))
print("Uppercase and lowercase count:", count_letters("Hello World"))
print("Square of list:", square_list([1, 2, 3, 4, 5]))
multiplication_table(5)
print("Sum of list:", sum_of_list())
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
print("Numbers divisible by 5:", divisible_by_5)
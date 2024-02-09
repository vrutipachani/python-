# 1. Create an empty dictionary called dog
dog = {}

# 2. Add name, color, breed, legs, age to the dog dictionary
dog["name"] = "Max"
dog["color"] = "Brown"
dog["breed"] = "Labrador"
dog["legs"] = 4
dog["age"] = 5

# 3. Create a student dictionary and add keys and values
student = {
    "first_name": "John",
    "last_name": "Doe",
    "gender": "Male",
    "age": 25,
    "marital_status": "Single",
    "skills": ["Python", "Java"],
    "country": "USA",
    "city": "New York",
    "address": "123 Main St"
}

# 4. Get the length of the student dictionary
student_length = len(student)
print("Length of student dictionary:", student_length)

# 5. Get the value of skills and check the data type
skills_value = student["skills"]
print("Type of skills:", type(skills_value))

# 6. Modify the skills values by adding one or two skills
student["skills"].extend(["C++", "JavaScript"])

# 7. Get the dictionary keys as a list
keys_list = list(student.keys())
print("Keys as a list:", keys_list)

# 8. Get the dictionary values as a list
values_list = list(student.values())
print("Values as a list:", values_list)

# 9. Change the dictionary to a list of tuples using items() method
student_tuples = list(student.items())
print("Dictionary as list of tuples:", student_tuples)

# 10. Delete one of the items in the dictionary
del student["marital_status"]

# 11. Delete one of the dictionaries
del dog

# Print updated student dictionary after deletion
print("Updated student dictionary after deletion:", student)
# 1. Declare an empty list
empty_list = []

# 2. Declare a list with more than 5 items
my_list = [1, 2, 3, 4, 5, 6, 7]

# 3. Find the length of your list
list_length = len(my_list)

# 4. Get the first item, the middle item, and the last item of the list
first_item = my_list[0]
middle_item = my_list[list_length // 2]
last_item = my_list[-1]

# 5. Declare a list called mixed_data_types
mixed_data_types = ["John", 30, 1.75, "Married", "123 Main St"]

# 6. Declare a list variable named it_companies
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]

# 7. Print the list
print("IT Companies:", it_companies)

# 8. Print the number of companies in the list
num_companies = len(it_companies)

# 9. Print the first, middle, and last company
first_company = it_companies[0]
middle_company = it_companies[num_companies // 2]
last_company = it_companies[-1]

# 10. Print the list after modifying one of the companies
it_companies[0] = "Meta"

# 11. Add an IT company to it_companies
it_companies.append("Intel")

# 12. Insert an IT company in the middle of the companies list
it_companies.insert(num_companies // 2, "Cisco")

# 13. Change one of the it_companies names to uppercase (IBM excluded!)
it_companies[4] = it_companies[4].upper()

# 14. Join the it_companies with a string '#;&nbsp; '
joined_companies = '#;&nbsp; '.join(it_companies)

# 15. Check if a certain company exists in the it_companies list.
company_to_check = "Apple"
company_exists = company_to_check in it_companies

# 16. Sort the list using sort() method
it_companies.sort()

# 17. Reverse the list in descending order using reverse() method
it_companies.reverse()

# 18. Slice out the first 3 companies from the list
first_three_companies = it_companies[:3]

# 19. Slice out the last 3 companies from the list
last_three_companies = it_companies[-3:]

# 20. Slice out the middle IT company or companies from the list
middle_index = len(it_companies) // 2
middle_company = it_companies[middle_index] if len(it_companies) % 2 != 0 else it_companies[middle_index - 1:middle_index + 1]

# 21. Remove the first IT company from the list
it_companies.pop(0)

# 22. Remove the middle IT company or companies from the list
del it_companies[middle_index]

# 23. Remove the last IT company from the list
it_companies.pop()

# 24. Remove all IT companies from the list
it_companies.clear()

# 25. Destroy the IT companies list
del it_companies

# 26. Join the following lists
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
full_stack = front_end + back_end

# 27. After joining the lists, insert Python and SQL after Redux
full_stack.insert(full_stack.index("Redux") + 1, "Python")
full_stack.insert(full_stack.index("Redux") + 2, "SQL")

print(full_stack)

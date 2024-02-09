# List of 10 students ages
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

# Sort the list and find the min and max age
ages.sort()
min_age = ages[0]
max_age = ages[-1]

# Add the min age and the max age again to the list
ages.extend([min_age, max_age])

# Find the median age
num_students = len(ages)
middle_index = num_students // 2
if num_students % 2 == 0:
    median_age = (ages[middle_index - 1] + ages[middle_index]) / 2
else:
    median_age = ages[middle_index]

# Find the average age
average_age = sum(ages) / num_students

# Find the range of the ages
age_range = max_age - min_age

# Compare the value of (min - average) and (max - average), use abs() method
min_average_diff = abs(min_age - average_age)
max_average_diff = abs(max_age - average_age)

# Find the middle country(ies) in the [countries list]
countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
num_countries = len(countries)
middle_country = countries[num_countries // 2] if num_countries % 2 != 0 else [countries[num_countries // 2 - 1], countries[num_countries // 2]]

# Divide the countries list into two equal lists if it is even if not one more country for the first half.
if num_countries % 2 == 0:
    first_half = countries[:num_countries // 2]
    second_half = countries[num_countries // 2:]
else:
    first_half = countries[:num_countries // 2 + 1]
    second_half = countries[num_countries // 2 + 1:]

# Unpack the first three countries and the rest as scandic countries
country1, country2, country3, *scandic_countries = countries[:3]

# Print results
print("Min age:", min_age)
print("Max age:", max_age)
print("Median age:", median_age)
print("Average age:", average_age)
print("Age range:", age_range)
print("Difference between min age and average age:", min_average_diff)
print("Difference between max age and average age:", max_average_diff)
print("Middle country(ies):", middle_country)
print("First half of countries:", first_half)
print("Second half of countries:", second_half)
print("First three countries:", country1, country2, country3)
print("Scandic countries:", scandic_countries)
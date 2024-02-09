# Unpack siblings and parents from family_members
siblings, parents = family_members[:num_siblings], family_members[num_siblings:]

print("Siblings:", siblings)
print("Parents:", parents)

# Create fruits, vegetables, and animal products tuples
fruits = ("apple", "banana", "orange")
vegetables = ("carrot", "lettuce", "tomato")
animal_products = ("meat", "milk", "egg")

# Join the three tuples and assign it to a variable called food_stuff_tp
food_stuff_tp = fruits + vegetables + animal_products

# Change the food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp)

# Slice out the middle item or items from the food_stuff_tp tuple or food_stuff_lt list
middle_index = len(food_stuff_tp) // 2
middle_items = food_stuff_tp[middle_index] if len(food_stuff_tp) % 2 != 0 else food_stuff_tp[middle_index - 1:middle_index + 1]

# Slice out the first three items and the last three items from food_stuff_lt list
first_three_items = food_stuff_lt[:3]
last_three_items = food_stuff_lt[-3:]

# Delete the food_stuff_tp tuple completely
del food_stuff_tp

# Check if an item exists in tuple
nordic_countries = ("Norway", "Sweden", "Finland", "Denmark", "Iceland")
print("'Estonia' is a Nordic country:", "Estonia" in⬤
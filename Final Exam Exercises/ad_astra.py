import re


# Read User input
food_info = input()
regex = r"(#|\|)([A-Za-z\s]+)\1([\d\/]+)\1(\d+)\1"
valid_info = re.findall(regex, food_info)

# Initialise data
calories_for_a_day = 2000
food_calories = 0

# Calculate food calories
for item in valid_info:
    food_calories += int(item[3])

# Calculate for how much days the calories are going to end
survive_days = food_calories // calories_for_a_day
print(f"You have food to last you for: {survive_days}!")

# Print every item and info for it
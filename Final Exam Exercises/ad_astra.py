import re


def print_something(command):
    calories_for_a_day = 2000
    food_calories = 0
    if command == "add": # Calculate for how much days the calories are going to end
        for item in valid_info:
            food_calories += int(item[3])
        survive_days = food_calories // calories_for_a_day
        print(f"You have food to last you for: {survive_days}!")

    elif command == "item":
        for item in valid_info:
            print(f"Item: {item[1]}, Best before: {item[2]}, Nutrition: {item[3]}")


# Read User input
food_info = input()
regex = r"(#|\|)([A-Za-z\s]+)\1([\d\/]+)\1(\d+)\1"
valid_info = re.findall(regex, food_info)

# Calculate food calories
print_something(command = 'add')

# Print every item and info for it
print_something(command = 'item')

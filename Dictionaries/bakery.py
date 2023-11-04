data_container = input().split()

initialised_dictionary = {}


for i in range(0, len(data_container), 2):
    food_key = data_container[i]
    quantities_value = int(data_container[i + 1])
    initialised_dictionary[food_key] = quantities_value

print(initialised_dictionary)
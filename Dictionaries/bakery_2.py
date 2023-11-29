data_container = input().split()

dictionary = {}

for i in range(0, len(data_container), 2):
    key = data_container[i]
    value = data_container[i+1]
    dictionary[key] = value

print(dictionary)
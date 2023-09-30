# Read User input
def linear_search(input_list, element):
    for i in range(len(my_list)):
        if my_list[i] == element:
            result = element
            return i
    return -1

my_list = [1, 3, 5, 7, 9, 11, 13]
element = 14

result = linear_search(my_list, element)
if result != -1:
    print(f'The target element {element} is at index {result}')
else:
    print(f'The target element {element} was not found in the list')

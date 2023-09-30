# Def Linear Searching Function
def linear_searching(your_list, element):
    for i in range(len(your_list)):
        if your_list[i] == element:
            result = i
            return result
    return -1

# Read Input
mylist = [int(x) for x in input().split(',')]
target = 7

# Call the function
result = linear_searching(mylist, target)

# Print function return
print(result)
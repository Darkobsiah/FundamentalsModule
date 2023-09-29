# Read User input
n = int(input())
special = input()
# Logic
my_list = []
special_list = []
for line in range(n):
    string = input()
    my_list.append(string)
print(my_list)
for line in range(len(my_list)):
    if 'SoftUni' in my_list[line]:
        special_list.append(my_list[line])
print(special_list)
# Print User output
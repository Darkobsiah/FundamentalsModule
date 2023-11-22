import re


racers = input(', ')
command = input()
people_names = []
sum = 0
people_info = {}
names_regex = r'([A-Za-z]+)'
number_regex = r'(\d+)'
while command != 'end of race':
    name_of_person = ''.join(re.findall(names_regex, command))

    if name_of_person not in people_names:
        people_names.append(name_of_person)
    kilometres = re.findall(number_regex, command)
    for x in kilometres:
        sum += int(x)
    if name_of_person not in people_info.keys():
        people_info[name_of_person] = sum
    else:
        people_info[name_of_person] += sum
    command = input()

print(people_info)
print()
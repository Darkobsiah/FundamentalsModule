data_input = input()

initialised_list = []
output_list = []

while True:
    if ':' not in data_input:
        searched_course = data_input
        break
    name, value, course = data_input.split(':')
    initialised_list.append({'student': {'name': name, 'value': value, 'course': course}})
    data_input = input()

print(initialised_list)
for element in initialised_list:
    for person, info in element.items():
        if searched_course in info['course']:
            output_list.append(info['name'])
            output_list.append(info['value'])

for i in range(0, len(output_list), 2):
    print(f'{output_list[i]} - {output_list[i+ 1]}')
total_effort = 0
type_and_values = []
list_of_values = []
type_and_values = input().split('#')
amount_of_water = int(input())
length = (len(type_and_values))
counter = 0
# Logic
for cell in type_and_values:
    element = cell.split(' = ')
    type_of_fire = element[0]
    integer_cell = element[1]
    current_amount = 0
    value_of_cell = int(integer_cell)
    if type_of_fire == 'High' and 81 < int(value_of_cell) < 125:
        if amount_of_water > value_of_cell:
            amount_of_water -= value_of_cell
            current_amount += value_of_cell * 0.25
            list_of_values.append(value_of_cell)

    elif type_of_fire == 'Medium' and 51 < value_of_cell < 80:
        if amount_of_water > value_of_cell:
            amount_of_water -= value_of_cell
            current_amount += value_of_cell * 0.25
            list_of_values.append(value_of_cell)

    elif type_of_fire == 'Low' and 1 < value_of_cell < 50:
        if amount_of_water > value_of_cell:
            amount_of_water -= value_of_cell
            current_amount += value_of_cell * 0.25
            list_of_values.append(value_of_cell)
    total_effort += current_amount
    counter += 1
    if cell == type_and_values[-1]: # Is it last?
        break
# Print the outputs
print('Cells:')
for each in list_of_values:
    print(' -', each)
print(f'Effort: {total_effort:.2f}')
total = sum(list_of_values)
print(f'Total Fire: {total}')
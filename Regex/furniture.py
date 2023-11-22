import re


# Initialise lists to store data
total_cost = []
furniture_list = []
# Regular expression
regex = r">+([A-Za-z]+)<<([0-9]+[\.0-9]*)!([0-9])"
furniture = input()
while furniture != 'Purchase':
    item_info = re.search(regex, furniture)
    if item_info:
        item_name = item_info[1]
        price = item_info[2]
        quantity = item_info[3]
        furniture_list.append(item_name)
        total_cost.append(float(price) * int(quantity))
    furniture = input()

# Print User output
print('Bought furniture:')
print('\n'.join(furniture_list))
print(f'Total money spend: {sum(total_cost)}')
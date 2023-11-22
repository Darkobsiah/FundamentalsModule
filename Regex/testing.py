import re


total_sum = 0
furniture_list = []
regex = r'>>([A-Za-z]+)<<(\d+\.?\d*)!(\d+)'
line = input()
while line != 'Purchase':
    result = re.search(regex, line)
    if result:
        item, price, quantity = result.groups()
        total_sum += float(price) * int(quantity)
        furniture_list.append(item)
    line = input()

print(f'Bought furniture:')
for furniture in furniture_list:
    print(furniture)
print(f'Total money spend: {total_sum:.2f}')
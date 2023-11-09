order_dictionary = {}

command = input()
while command != 'buy':
    name, price, quantity = command.split()
    if name not in order_dictionary:
        order_dictionary[name] = [price, quantity]
    else:
        order_dictionary[name][quantity] += quantity
        order_dictionary[name][price] = price

    command = input()

for name, lst in order_dictionary.items():
    values = ''
    print(f'{name} -> {q * p}')



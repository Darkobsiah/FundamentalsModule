order_dictionary = {}

command = input()
while command != 'buy':
    name, price, quantity = command.split()
    price = float(price)
    quantity = float(quantity)
    if name not in order_dictionary:
        order_dictionary[name] = [price, quantity]
    else:
        order_dictionary[name][0] += price
        order_dictionary[name][1] = quantity

    command = input()

for name, lst in order_dictionary.items():
    values = ''
    money = 0
    counter = 0
    for value in lst:
        if counter == 0:
            money += float(value)
        else:
            money *= float(value)
        counter += 1
    print(f'{name} -> {money:.2f}')



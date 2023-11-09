order_dictionary = {}

command = input()
while command != 'buy':
    name, (price), quantity = command.split()
    if name not in order_dictionary:
        order_dictionary[name] = [float(price), quantity]
    else:
        order_dictionary[name][0][1] += quantity
        order_dictionary[name][1] = price

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



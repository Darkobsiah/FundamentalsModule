single_string = input()
numbers = []
letters = []

for symbol in single_string:
    if symbol.isnumeric():
        numbers.append(symbol)
        single_string = single_string.replace(symbol, '')
    elif symbol.isalpha():
        letters.append(symbol)
        single_string = single_string.replace(symbol, '')

print(''.join(numbers))
print(''.join(letters))
print(single_string)
symbols = [character for character in input() if character != ' ']

some_dict = {}

for symbol in symbols:
    if symbol not in some_dict:
        some_dict[symbol] = 0
    some_dict[symbol] += 1

for key, value in some_dict.items():
    print(f"{key} -> {value}")
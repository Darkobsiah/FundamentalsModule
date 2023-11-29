def lowering(string: str)-> str:
    return string.lower()


def uppering(string: str)-> str:
    return string.upper()


some_list = ['Pesho', 'GOSHO', 'mitko']

# Lowering function called
lowered_list = list(map(lowering, some_list))
print(lowered_list)

upper_list = list(map(uppering, some_list))
print(upper_list)
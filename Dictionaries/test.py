people = {
    'Slavi': {'height': 185, 'weight': 72},
    'Ivan': {'height': 184, 'weight': 74},
    'Nasko': {'height': 178, 'weight': 73}
}

for name, info in people.items():
    print(f'---{name}---')
    for param, value in info.items():
        if param == 'height':
            print(f'{param} - {value}sm')
        else:
            print(f'{param} - {value}kg')

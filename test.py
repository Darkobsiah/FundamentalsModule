names = ['Slavi', 'Nasko','Dobi']


def name_validator(name):
    if len(name) < 5:
        print(f'{name} shorter than 5 symbols')
        return False
    return True



access = filter(name_validator, names)
for name in access:
    print(f'{name} has access.')



data = 'TeXt'

print('Lowercase:', data.lower())
print('Lowercase:', data.casefold())  # just as lower()
print('Uppercase:', data.upper())
print()

print('If data is digit:', data.isdigit())

name = 'slavi'
print(name.capitalize())   # first letter -> upper()
print()

greeting = ' hello '
print(greeting.lstrip())   # removes the left space
print(greeting.rstrip())  # removes the r space
print(greeting.strip())   # remove the both spaces
print()

print(name.startswith('S'))
print(name.capitalize().startswith('S'))
print(name.endswith('i'))

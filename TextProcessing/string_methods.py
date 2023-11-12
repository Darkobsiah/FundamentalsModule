data = 'TeXt'

print('Lowercase:', data.lower())
print('Lowercase:', data.casefold())  # just as lower()
print('Uppercase:', data.upper())
print('If data is digit:', data.isdigit())
print()

greeting = ' hello '
print(greeting.lstrip())   # removes the left space
print(greeting.rstrip())  # removes the r space
print(greeting.strip())   # remove the both spaces
print()


name = 'slavi'
print(name.capitalize())   # first letter -> upper()
print(name.startswith('S'))   # False
print(name.capitalize().startswith('S'))   # True
print(name.endswith('i'))
print()


text = 'hello world'
print(text.index('o'))
# check if the string has upper letters
print(text.isalpha())
# check if the string is from numbers
print(text.isnumeric())

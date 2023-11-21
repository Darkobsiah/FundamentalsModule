import re

numbers = ''
regex = r'\d+'
command = input()
while command:
    numbers = re.findall(regex, command)
    for num in numbers:
        print(int(num), end=' ')
    command = input()


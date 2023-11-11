some_dict = {}

while True:
    command = input()
    if command == 'end of contests':
        break
    contest, password = command.split(':')
    some_dict[contest] = password



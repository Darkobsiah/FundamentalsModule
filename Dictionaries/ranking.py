courses = {}


while True:
    command = input()
    if command == 'end of contests':
        break
    contest, password = command.split(':')
    courses[contest] = password


while True:
    is_valid = True

    command = input()
    if command == 'end of submissions':
        break

    contest, password, username, points = command.split('=>')
    if contest not in courses.keys():
        is_valid = False
    elif courses[contest] != password:
        is_valid = False
    else:




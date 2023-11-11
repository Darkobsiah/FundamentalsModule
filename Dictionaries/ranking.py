courses = {}
users_memory = {}

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
    else:   # Valid contest and password
        if username not in users_memory:
            users_memory[username] = []
        users_memory[username].append({'username': username,
                                       'contest': contest,
                                       'points': 0})
        if username[username]['points'] < password:
            username[username]['points'] = password

most_valuable_user = ''
for


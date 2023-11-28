saved_data = {}

while True:
    command = input()
    if command == 'end of contests':
        break

    contest, password = command.split(":")
    saved_data[contest] = {'password': password}

print(saved_data)

athletes_data = {}
while True:
    command = input()
    if command == 'end of submissions':
        break

    contest, password, username, points = command.split("=>")
    if contest in saved_data:
        if saved_data[contest]['password'] == password:
            if username not in athletes_data:
                athletes_data[contest] = {username: 0}
            athletes_data[contest][username] += int(points)

print(athletes_data)
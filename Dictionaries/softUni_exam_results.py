data_dict = {}
banned_users = []
java = 0
c_sharp = 0

# endless loop
while 1:
    command = input()
    if not command[0] in banned_users:
        # break condition
        if 'exam finished' in command:
            break
        if 'banned' in command:
            command = command.split('-')
            banned_users.append(command[0])
            continue
        command = command.split('-')
        name = command[0]
        language = command[1]
        points = command[2]
        if name not in data_dict.keys():
            data_dict[name] = {"language": language,
                               "points": points}
    if language == 'Java':
        java += 1
    elif language == 'C#':
        c_sharp += 1

print('Results:')
for key, values in data_dict.items():
    if key not in banned_users:
        print(f"{key} | {data_dict[key]['points']}")
print('Submissions:')
print(f'Java - {java}')
print(f'C# - {c_sharp}')


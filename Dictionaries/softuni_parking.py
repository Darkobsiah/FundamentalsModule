parking_users_info = {}
number_of_commands = int(input())
counter = 0
while counter < number_of_commands:
    command = input()
    if 'unregister' in command:
        command, username = command.split()
        if username in parking_users_info.keys():
            print(f"{username} unregistered successfully")
            parking_users_info.pop(username)
        else:
            print(f"ERROR: user {username} not found")

    else:
        command, username, plate_num = command.split()
        if username in parking_users_info.keys():
            print(f"ERROR: already registered with plate number {plate_num}")
        else:
            parking_users_info[username] = [plate_num]
            print(f"{username} registered {plate_num} successfully")
    counter += 1

for key, value in parking_users_info.items():
    print(f"{key} => {''.join(value)}")
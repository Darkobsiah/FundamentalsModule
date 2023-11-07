force_side_users = {}
command = input()

while command != 'Lumpawaroo':

    if '|' in command:
        force_side, force_user = command.split(" | ")
        if force_side_users:
            for key, value in force_side_users.items():
                if force_user in value:
                    break
                if force_side not in key:
                    force_side_users[force_side] = []
                    force_side_users[force_side].append(force_user)
                    break
        else:
            force_side_users[force_side] = []
            force_side_users[force_side].append(force_user)

    elif '->' in command:
        force_user, force_side = command.split(" -> ")
        for value in force_side_users.values():
            if force_user not in value:
                force_side_users[force_side] = []
            else:
                force_side_users[force_side] = force_side
                print(f'{force_user} joins the {force_side} side!')
            force_side_users[force_side].append(force_user)
    command = input()

for key, value in force_side_users.items():
    if key:
        print(f'Side: {key}, Members: {len(value)}')
        for s in value:
            print(f'! {s}')

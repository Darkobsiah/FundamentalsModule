force_book = {}

while True:
    command = input()
    if command == 'Lumpawaroo':
        break
    if "|" in command:
        force_side, force_user = command.split(' | ')
        user_is_part_of_the_force = False
        for value in force_book.values():
            if force_user in value:
                is_there = True

        if not user_is_part_of_the_force:
            if force_side not in force_book:
                force_book[force_side] = []
            force_book[force_side].append(force_user)

    elif "->" in command:
        force_user, force_side = command.split(' -> ')
        if force_user in force_book:
            force_book.pop(force_user)
            force_book[force_side].append(force_user)
        else:



groceries_list = input().split("!")

command = input()
while True:
    if command == 'Go Shopping!':
        break
    command = command.split()
    type_of_command = command[0]
    if type_of_command == 'Urgent':
        item = command[1]
        if item not in groceries_list:
            groceries_list.insert(item, 0)

    elif type_of_command == 'Unnecessary':
        item = command[1]
        if item in groceries_list:
            groceries_list.remove(item)

    elif type_of_command == 'Correct':
        old_item = command[1]
        new_item = command[2]
        if old_item in groceries_list:
            index = groceries_list.index(old_item)
            groceries_list[index] = new_item

    elif type_of_command == 'Rearrange':
        item = command[1]
        if item in groceries_list:
            groceries_list.remove(item)
            groceries_list.append(item)

    command = input()

print(', '.join(groceries_list))
# Read User input
stops = input()

# Logic
command = input()
while command != 'Travel':  # Manipulate the string
    command = command.split(':')
    action = command[0]

    if action == 'Add Stop':
        pass
    elif action == 'Remove Stop':
        pass
    elif action == 'Switch':
        pass


    command = input()
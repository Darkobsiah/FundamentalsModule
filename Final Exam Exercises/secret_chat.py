# Read User input
conceal_message = input()

command = input()
# Initialise a while loop
while command != "Reveal":
    command = command.split(":|:")
    if command[0] == 'InsertSpace':
        index = int(command[1])
        conceal_message = conceal_message[:index] + ' ' + conceal_message[index:]

    elif command[0] == 'Reverse':
        substring = command[1]
        if substring in conceal_message:
            conceal_message = conceal_message.replace(substring, '')
            conceal_message += substring[::-1]
    elif command[0] == 'ChangeAll':
        substring, replacement = command[1], command[2]
        conceal_message = conceal_message.replace(substring, replacement)
    command = input()

print(f'You have a new text message: {conceal_message}')
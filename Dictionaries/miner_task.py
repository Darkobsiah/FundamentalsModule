# Initialise a While loop
counter = 0
miner_dictionary = {}
last_command = ''

while True:
    command = input()
    # increment by 1 with every input
    counter += 1

    # implement ending condition
    if command == 'stop':
        break

    if counter % 2 != 0:
        # resource one (even)
        miner_dictionary[command] = ''
    else:
        # if counter is even
        # adding the quantity of the given resource
        miner_dictionary[last_command] = command
    # save the name of the resource
    last_command = command

# Print the output
for key, value in miner_dictionary.items():
    print(f'{key} -> {value}')

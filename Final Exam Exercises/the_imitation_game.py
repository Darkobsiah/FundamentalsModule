# Define the functions first
def move_letters(message: str, num_of_letters: int) -> str:
    """
    Initialise a function that Moves the first n
    letters to the back of the string
    :param message: str
    :param num_of_letters: int
    :return: str
    """
    message = message[number_of_letters:] + message[:number_of_letters]
    return message


def insert_index(message: str, index_m: int, value_m: str) -> str:
    """
    Initialise a function that Inserts the given value
    before the given index
    :param message: str
    :param index_m: int
    :param value_m: str
    :return: str
    """
    message_list_of_letters = [x for x in message]
    message_list_of_letters.insert(index_m, value_m)
    return ''.join(message_list_of_letters)


def change_all(message: str, old: str, new: str):
    """
    Change all occurrences of the given substring
    # with the replacement text
    :param message: str
    :param old: str
    :param new: str
    :return: str
    """
    message = message.replace(old, new)
    return message


def main_func(encmsg: str, commands: list):
    for command in commands:
    if 'Move' in command:
        number_of_letters = int(command.split('|')[-1])
        encrypted_message = move_letters(encrypted_message, number_of_letters)

    elif 'Insert' in command:
        command, index, value = command.split('|')
        encrypted_message = insert_index(encrypted_message, int(index), value)

    elif 'ChangeAll' in command:
        command, substring, replacement = command.split('|')
        encrypted_message = change_all(encrypted_message, substring, replacement)


# Read User input
encrypted_message = input()
command_list = []
# Logic
while True:
    command = input()
    if command == 'Decode':
        break
    command_list.append(command)

# Print Main function output
print(main_func(encrypted_message, command))

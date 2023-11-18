def move_letters(message: str, number: int) -> str:
    """
    Initialise a function that Moves the first n
    letters to the back of the string
    :param message: str
    :param number: int
    :return: str
    """
    substring = message[:number]
    left_string = message[number:]
    new_string = left_string + substring
    return new_string


def insert_index(message: str, index: int, value: str) -> str:
    """
    Initialise a function that Inserts the given value
    before the given index
    :param message: str
    :param index: int
    :param value: str
    :return: str
    """
    message_list_of_letters = [x for x in message]
    message_list_of_letters.insert(index, value)
    return ''.join(message_list_of_letters)


def change_all(message: str, old: str, change: str):


# COME ON LET'S DO THIS
encrypted_message = input()
while True:
    command = input()
    if encrypted_message == 'Decode':
        break

    # Moves the first n letters to the back of the string
    if 'Move' in command:
        number_of_letters = int(command.split('|')[-1])
        print(move_letters(encrypted_message, number_of_letters))

    # Inserts the given value before the given index
    elif 'Insert' in command:
        command, index, value = command.split('|')
        print(insert_index(encrypted_message, int(index), value))

    # Change all occurrences of the given substring
    # with the replacement text
    elif 'ChangeAll' in command:
        command, substring, replacement = command.split('|')
        print(change_all(encrypted_message, substring, replacement))
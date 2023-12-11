def valid_length(users: list):
    """
    This functions check the valid of the string
    within the list and returns it only with validated ones
    :param users: lists
    :return: list
    """
    loop_list = users.copy()
    for name in loop_list:
        if 3 < len(name) < 16:
            continue
        else:
           users.remove(name)
    return users


def valid_contains(users: list):
    """
        This functions check what string in the list
        contains and keep only these with letters and nums
        :param users: lists
        :return: list
    """
    loop_list = users.copy()
    for user in loop_list:
        for letter in user:
            if letter.isalnum() or letter == '-' or letter == '_':
                continue
            else:
                users.remove(user)
                break
    return users


def redundant_symbols_check(users: list):
    """
        This functions check if the string within the list
        contains Space or not, returns a list only whit these
        who does not
        :param users: lists
        :return: list
    """
    loop_list = users.copy()
    for user in loop_list:
        if ' ' in user:
            users.remove(user)
    return loop_list


def username_validator(users: list):
    """
    This is our main function. Here we only
    call the other one which are described above.
    :param users: lists
    :return: list
    """
    valid_length(users)
    valid_contains(users)
    redundant_symbols_check(users)
    return users


# Read User input
usernames = input().split(', ')
valid_usernames = username_validator(usernames)
# Print User output
print('\n'.join(valid_usernames))

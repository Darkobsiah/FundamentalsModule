def valid_length(users: list, valid_names):
    for name in users:
        if 3 < len(name) < 16:
            valid_names.append(name)
        else:
            continue
    return users


def valid_contains(users: list, valid_names):
    for user in users:
        for letter in user:
            print(letter)


def username_validator(users: list):
    valid_names = []
    valid_length(users, valid_names)
    valid_contains(users, valid_names)


# Read User input
usernames = input().split(', ')
username_validator(usernames)

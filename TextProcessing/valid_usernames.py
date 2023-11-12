# Read User input
usernames = input().split(', ')
valid_usernames = []

for username in usernames:
    is_valid = True
    if 3 > len(username):
        is_valid = False
    elif 16 < len(username):
        is_valid = False
    if not is_valid:
        continue

    for symbol in username:
        if symbol.isalpha() or symbol.isnumeric() or symbol == '-' or symbol == '_':
            continue
        else:
            is_valid = False
            break
    if is_valid:
        valid_usernames.append(username)

print(' '.join(valid_usernames))

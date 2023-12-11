# Read User input
usernames = input().split(', ')
valid_usernames = []

# Initialise a for-loop
for username in usernames:
    is_valid = True
    if 3 > len(username):
        is_valid = False
    elif 16 < len(username):
        is_valid = False
    # is false - break condition
    if not is_valid:
        continue

    # Initialise a nested for-loop
    for symbol in username:
        if symbol.isalpha() or symbol.isnumeric() or symbol == '-' or symbol == '_':
            continue
        else:
            # is false - break condition
            is_valid = False
            break
    if is_valid:
        valid_usernames.append(username)

# Print User output
print('\n'.join(valid_usernames))

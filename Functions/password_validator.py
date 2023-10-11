# Define a function
def password_validator(special: str):
    valid = True
    if 6 > len(special) > 10:
        valid = False

    # Make the letter or digits check
    for symbol in special:
        if 0 < ord(symbol) < 47:
            valid = False
        if 65 < ord(symbol) < 90:
            valid = False

    # Check for 2 digits at least
    return True



# Read User input
password = input()


# Print the result of the function
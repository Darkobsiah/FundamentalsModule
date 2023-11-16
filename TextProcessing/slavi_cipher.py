def encrypting_algorithm(user_profiles, password, key):
    key = random.randint(1, 33)
    encrypted_message = ''
    for symbol in password:
        encrypted_message += chr(ord(symbol) + key)
    user_profile[name] = {encrypted_message: key}

import random
# Read User Message
name = input('Please enter your name: ')
password = input('Now your password: ')
user_profile = {}

# Call the Encrypting Algorithm function
encrypting_algorithm(user_profile, password, key)

user_profile[name] = {encrypted_message: key}
print(user_profile)
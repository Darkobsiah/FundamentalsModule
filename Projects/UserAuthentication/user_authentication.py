from cryptography.fernet import Fernet

user_credentials = {}
user_profile_info = {}


def save_credentials(user, password, credentials):
    credentials[user] = {'pass': password}
    print(credentials)
    return True


def encrypt_decrypt_messages(command, username, password, credentials):
    if command == 'encrypt':
        key = Fernet.generate_key()
        fernet = Fernet(key)

        # then use the Fernet class instance
        # to encrypt the string string must
        # be encoded to byte string before encryption
        encMessage = fernet.encrypt(password.encode())

        credentials[username] = {'key': key, 'encMessage': encMessage}
        print(credentials)
    else:
        fernet = Fernet(credentials['key'])
        # decrypt the encrypted string with the
        # Fernet instance of the key,
        # that was used for encrypting the string
        # encoded byte string is returned by decrypt method,
        # so decode it to string with decode methods
        decMessage = fernet.decrypt(password).decode()
        print(credentials)
        print("decrypted string: ", decMessage)


def password_validator(username: str, user_pass: str, credentials: dict):
    valid = True
    special = user_pass.lower()
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                "u", "v", "w", "x", "y", "z"]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    integer_counter = 0
    if 6 > len(special) or 10 < len(special):
        print('Password must be between 6 and 10 characters')
        valid = False
    for symbol in special:
        if symbol not in alphabet:
            if symbol not in numbers:
                print('Password must consist only of letters and digits')
                valid = False
        if symbol in numbers:
            integer_counter += 1

    if integer_counter < 2:
        print('Password must have at least 2 digits')
        valid = False
    if valid:
        print('Password is valid')
        return True
    else:
        return ''


def main():
    log_or_reg = input('Hello user, if you already have an account input /log/'
                       'otherwise, write the following in the console /reg/')
    if log_or_reg.lower() == 'log':
        name = input('Name: ')
        while True:
            password = input('Enter password: ')

            if password_validator(name, password, user_credentials):
                break

        save_credentials(name, password, user_credentials)
    elif log_or_reg


if __name__ == '__main__':
    main()

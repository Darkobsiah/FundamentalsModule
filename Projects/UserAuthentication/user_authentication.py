from cryptography.fernet import Fernet

user_credentials = {}
user_profile_info = {}


def register_user(credentials: dict, user_profile):
    name = input('\nEnter a username: ')
    passes = False
    while 1:
        if name not in user_credentials.keys():
            password1 = input('Enter password: ')
            if password_validator(name, password1, user_credentials):
                while True:
                    password2 = input('Enter it again: ')
                    if password1 == password2:
                        passes = True
                        break
                    else:
                        print('Invalid try to repeat the password. Try with another one.\n')
                        break

                if passes:
                    break
    save_credentials(name, password2, user_credentials)
    add_user_info(name, user_credentials, user_profile)
    print(f'\n---------------------------------------\n'
          f'Your profile has been created, {name}!\n'
          f'---------------------------------------')
    return True


def login_user(credentials: dict):
    while True:
        name = input('Please enter your username here: ')
        if name in credentials.keys():
            pass
        else:
            print('This username have no account in the server.\n')
            answer = ('If you want register one write /m/\n'
                      'but on purpose to input a new one use /n/')
            if answer.lower() == 'm':
                main()
            elif answer == 'n':
                continue


def add_user_info(username, credentials, user_profiles):
    name = input('\nEnter first and last name: ')
    age = input('\nEnter your age: ')
    place = input('\nWhere do you live at the moment: ')

    user_profiles[username] = {'name': name, 'age': age, 'place': place}
    return user_profiles


def save_credentials(user, password, credentials):
    credentials[user] = {'pass': password}
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
    log_or_reg = input('\nHello user, if you already have an account input /log/\n'
                       'otherwise, write the following in the console /reg/: ')
    if log_or_reg.lower() == 'register' or log_or_reg.lower() == 'reg':
        register_user(user_credentials, user_profile_info)

    elif log_or_reg.lower() == 'login' or log_or_reg.lower() == 'log':
        login_user(user_credentials)



if __name__ == '__main__':
    main()

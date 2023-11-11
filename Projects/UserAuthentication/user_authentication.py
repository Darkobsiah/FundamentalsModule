from cryptography.fernet import Fernet

user_credentials = {}
user_profile_info = {}


def encrypt_decrypt_messages(command, username, password, credentials):
    if command == 'encrypt':
        key = Fernet.generate_key()
        variable = Fernet(key)

        # then use the Variable class instance
        # to encrypt the string string must
        # be encoded to byte string before encryption
        enc_message = variable.encrypt(password.encode())

        credentials[username] = {'key': key, 'encMessage': enc_message}
        print(credentials)
    else:
        variable = Fernet(credentials['key'])
        # decrypt the encrypted string with the
        # Variable instance of the key,
        # that was used for encrypting the string
        # encoded byte string is returned by decrypt method,
        # so decode it to string with decode methods
        dec_message = variable.decrypt(password).decode()
        print(credentials)
        print("decrypted string: ", dec_message)


def password_validator(user_pass: str):
    valid = True
    special = user_pass.lower()
    alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
                "u", "v", "w", "x", "y", "z"]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    integer_counter = 0
    if 6 > len(special) or 10 < len(special):
        print('Password must be between 6 and 10 characters.')
        valid = False
    for symbol in special:
        if symbol not in alphabet:
            if symbol not in numbers:
                print('Password must consist only of letters and digits.')
                valid = False
        if symbol in numbers:
            integer_counter += 1

    if integer_counter < 2:
        print('Password must have at least 2 digits.')
        valid = False
    if valid:
        print('\nPassword is valid.')
        return True
    else:
        return ''


def register_user(credentials: dict, user_profile: dict):
    while True:
        name = input('\nEnter a username: ')
        if name not in credentials.keys():
            break
        else:
            print(f'This username has been already used')
            print('Please choose another one')

    passes = False
    while 1:
        password1 = input('Enter a password: ')
        if password_validator(password1):
            counter = 3
            while True:
                password2 = input('Enter the same password: ')
                if password1 == password2:
                    passes = True
                    break
                else:
                    counter -= 1
                    if counter <= 0:
                        break
                    print('\nIncorrect try to repeat your password!')
                    print(f'{counter} tries left.')
                    continue
        else:
            continue
        if passes:
            break
        else:
            print(f'\nUnfortunately you failed to repeat your password. Try again with new one!')
    credentials[name] = {'pass': password1}
    print('\nPassword was saved successfully.')
    add_user_info(name, user_profile)

    print(f'\n---------------------------------------\n'
          f'-Your profile has just been created, {name}!\n'
          f'---------------------------------------')

    print('\nNow you should login.')
    log_user_in(credentials)
    return True


def add_user_info(username: str, user_profiles: dict):
    print('\nPlease give us some details about yourself.')
    name = input('Enter first and last name: ')
    age = input('Enter your age: ')
    place = input('Which country do you live in: ')

    user_profiles[username] = {'Name': name, 'Age': age, 'Country': place}
    return user_profiles


def log_user_in(credentials: dict):
    while True:
        username = input('\nPlease, enter your username here: ')
        if username in credentials.keys():
            password = credentials[username]['pass']
            counter = 3
            while counter > 0:
                user_input = input('Enter your password: ')
                if user_input == password:
                    show_user_info(username, user_profile_info)
                else:
                    counter -= 1
                    print('\nIncorrect password!')
                    print(f'{counter} tries left.')
                    continue
        else:
            print('\nError: No such user in the server.\n')
            answer = input('If you want register one, write - (r)\n'
                           'In case that you already have an account\n'
                           '                 try again with - (a) ')
            if answer.lower() == 'r':
                register_user(credentials, user_profile_info)
            elif answer == 'a':
                continue


def show_user_info(username: str, profiles_info: dict):
    print(f'\nYou had successfully logged into your account, {username}!')
    print('|Profile info:')
    print('|--------------------------------------------------|')
    for key, value in profiles_info[username].items():
        print(f'| {key} - {value}')
    print('|--------------------------------------------------|')
    after_login()


def after_login():
    while True:
        user_input = input('\nTo add more info about you, enter (i)\n'
                           'and Exit the program with (e): ')
        if user_input.lower() == 'i':
            pass
        elif user_input.lower() == 'm':
            main()
        elif user_input.lower() == 'e':
            exit()
        else:
            print('Error: Invalid input')


def main():

    log_or_reg = input('\nHello user, if you already have an account input /log/\n'
                       'otherwise, write the following in the console /reg/: ')

    if log_or_reg.lower() == 'register' or log_or_reg.lower() == 'reg':
        register_user(user_credentials, user_profile_info)

    elif log_or_reg.lower() == 'login' or log_or_reg.lower() == 'log':
        log_user_in(user_credentials)

    else:
        print(f'\nError: Invalid answer / Please try again...')
        main()


if __name__ == '__main__':
    main()





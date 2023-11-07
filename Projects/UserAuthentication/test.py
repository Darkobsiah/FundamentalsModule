from cryptography.fernet import Fernet
import getpass


def encrypting(message):
    key = Fernet.generate_key()
    f = Fernet(key)
    encrypt_token = f.encrypt(b'')
    print(encrypt_token)

    decrypt_token = f.decrypt(encrypt_token)
    print(decrypt_token)

password = input('Enter password: ')
encrypting(password)

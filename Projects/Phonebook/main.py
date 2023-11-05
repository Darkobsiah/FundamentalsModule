address_book = {}


def add_contact():
    name = input('Enter the name: ')
    phone = input('Enter the phone number: ')
    address = input('Enter the address: ')
    address_book[name] = {'Phone' : phone, 'Address': address}
    print(f'Contact {name} has been added!')


def show_contacts():
    print('\nList of your contacts:')
    for name in address_book:
        print(name,end=' ')
        print('')
    answer = input('\nDo you want to be returned to the Main menu? (y/n): ')
    while True:
        answer = answer.lower()
        if answer == 'y' or answer == 'yes' or answer == '(y)' or answer == '(yes)':
            return True
        elif answer == 'n' or answer == 'no' or answer == '(n)' or answer == '(yes)':
            sure = input('\nAre you sure you want to exit the program?\n'
                         '-------y------------or------------n-------: ')
            if sure == 'y' or sure == 'yes' or sure == '(y)' or sure == '(yes)':
                exit_program()
            elif answer == 'n' or answer == 'no' or answer == '(n)' or answer == '(yes)':
                answer = input('\nDo you want to be returned to the Main menu? (y/n): ')
                if answer == 'y' or answer == 'yes' or answer == '(y)' or answer == '(yes)':
                    break
                elif answer == 'n' or answer == 'no' or answer == '(n)' or answer == '(yes)':
                    continue
                else:
                    answer = input('\nYour answer is invalid please choose between (y) or (n)')
        else:
            answer = input('\nYour answer is invalid please choose between (y) or (n)')


def search_contacts():


def exit_program():
    print('\nThank you for using our ContactBook,\n'
          '**************Goodbye!**************')
    exit()


while True:
    print('\nAddress Book Menu:')
    print('1. Add Contact')
    print('2. Show Contacts')
    print('3. Search Contact')
    print('4. ')
    print('5. Exit Menu')
    choice = input('Please enter your choice (1/2/3/4/5): ')

    if choice.isnumeric():
        if int(choice) == 1:
            add_contact()
        elif int(choice) == 2:
            show_contacts()
        elif int(choice) == 3:
            search_contacts()
        elif int(choice) == 4:
            ...
        elif int(choice) == 5:
            print('Goodbye summoner!')
            break
        else:
            print('Your chose is invalid.'
                  'Please use only 1, 2, 3, 4 or 5')
    else:
        print('\nYour chose is invalid.'
              'Please use only 1, 2, 3, 4 or 5')

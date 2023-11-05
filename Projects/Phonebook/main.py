address_book = {}


def add_contact():
    name = input('Enter the name: ')
    phone = input('Enter the phone number: ')
    address = input('Enter address: ')
    address_book[name] = {'Phone' : phone, 'Address': address}
    print(f'Contact {name} has been added!')


def show_contacts():
    print('\nList of your contacts:')
    for name in address_book:
        print(f"- {name}",end=' ')
        print('')
    answer = input('\nDo you want to be returned to the Main Menu? (y/n): ')
    while True:
        answer = answer.lower()
        if answer == 'y' or answer == 'yes' or answer == '(y)' or answer == '(yes)':
            return True
        elif answer == 'n' or answer == 'no' or answer == '(n)' or answer == '(yes)':
            sure = input('\nAre you sure you want to exit the program?\n'
                         '-------( y )---------or---------( n )-------: ')
            if sure == 'y' or sure == 'yes' or sure == '(y)' or sure == '(yes)':
                exit_program()
            elif answer == 'n' or answer == 'no' or answer == '(n)' or answer == '(yes)':
                answer = input('\nDo you want to be returned to the Main menu? (y/n): ')
                if answer == 'y' or answer == 'yes' or answer == '(y)' or answer == '(yes)':
                    break
                elif answer == 'n' or answer == 'no' or answer == '(n)' or answer == '(yes)':
                    continue
                else:
                    answer = input('\nYour answer is invalid, please choose between (y) and (n): ')
        else:
            answer = input('\nYour answer is invalid, please choose between (y) and (n): ')


def search_contacts():
    while True:
        contact = input('Enter contact here: ')
        if contact in address_book:
            print(f'\nContact found,')
            print(f"Phone - {address_book[contact]['Phone']},\nAddress - {address_book[contact]['Address']}.")
        else:
            print('\nThis contact does not exist')
        answer = input(f'\nIf you want to search again choose (a)\n'
                       f'and to go back to Main Menu choose (m): ')
        while True:
            answer = answer.lower()
            if answer == 'm':
                return True
            elif answer == 'a':
                break
            else:
                answer = input('\nYour answer is invalid, please choose between\n'
                               '(a) for another try,\n'
                               '(m) to return back to Main Menu.')


def delete_contact():
    name = input('Write the name of the contact you would like to delete: ')
    if name in address_book:
        address_book.pop(name)
        print(f'\n{name} was deleted from your Phonebook.')
        choose = input('\nIf you have the desire to delete more contacts choose (d),\n'
                       'Otherwise in a way to return back to Main Menu choose (m):  ')


def exit_program():
    print('\nThank you for using our ContactBook,\n'
          '************__Goodbye!__************')
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
            delete_contact()
        elif int(choice) == 5:
            print('\nGoodbye, Dear User!')
            break
        else:
            print('\nYour chose is invalid.'
                  'Please use only 1, 2, 3, 4 or 5')
    else:
        print('\nYour chose is invalid.'
              'Please use only 1, 2, 3, 4 or 5')

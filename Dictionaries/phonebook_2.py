phonebook = {}

while True:
    command = input()
    if '-' not in command:
        n = int(command)
        break

    name, phone_number = command.split('-')
    if name not in phonebook:
        phonebook[name] = ''
    phonebook[name] = phone_number

for search in range(n):
    searched_name = input()
    if searched_name in phonebook:
        print(f"{searched_name} -> {phonebook[searched_name]}")
    else:
        print(f"Contact {searched_name} does not exist.")
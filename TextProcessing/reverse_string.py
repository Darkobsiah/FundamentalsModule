while True:
    some_string = input()

    if some_string.lower() == 'end':
        break

    print(some_string[::-1])

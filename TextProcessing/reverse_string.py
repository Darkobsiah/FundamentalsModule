# Initialise a while loop
while True:
    some_string = input()

    if some_string.lower() == 'end':
        break
# use slicing to reverse the str
    print(some_string[::-1])

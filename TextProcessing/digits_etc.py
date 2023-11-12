# Read User input
text = input()

numbers = ''
letters = ''
others = ''

# Initialising a for loop
for s in text:
    if s.isnumeric():
        numbers += s
    elif s.isalpha():
        letters += s
    else:
        others += s

# Print the symbols to the User
print(numbers)
print(letters)
print(others)
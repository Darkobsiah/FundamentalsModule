text = input()

digits = ''
letters = ''
other = ''

for c in text:
    if c.isnumeric():
        digits += c
    elif c.isalpha():
        letters += c
    else:
        other += c

print(digits)
print(letters)
print(other)
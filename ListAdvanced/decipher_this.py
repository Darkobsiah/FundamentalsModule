secret_message = input().split()

for word in secret_message:
    alphabetic = []
    numerics = []
    number = ''

    for digit in word:
        if digit.isnumeric():
            numerics.append(digit)

        if digit.islower():
            alphabetic.append(digit)
    print(numerics)
    print(word)




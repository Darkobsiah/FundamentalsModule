# Read User input
combination = input()

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'v','k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x',
            'y', 'z']

def number_in_alphabet(text: str, char: str, letter_list: list) -> int:
    is_found = False
    my_letter = text[char]
    my_letter.lower()
    counter = 0
    for letter in alphabet:
        if letter == my_letter:
            is_found = True
        counter += 1
        if is_found:
            return counter
        return True


number = ''
characters = ''
# Found the letters and the numbers
# in the string and initialise them
# in different strings
for index in combination:
    if index.isnumeric():
        number += index
    else:
        characters += index
number = int(number)
total_sum = number

final_count = 0
for character in characters:
    if final_count == 0:
        if character.isupper():
            alphabetic_num = number_in_alphabet(combination, character, alphabet)
            total_sum = total_sum // alphabetic_num
        else:
            alphabetic_num = number_in_alphabet(combination, character, alphabet)
            total_sum += number * alphabetic_num
    else:
        if character.isupper():
            total_sum -= combination[-1]
        else:
            total_sum += combination[-1]
    final_count += 1

print(total_sum)





# Read User input
string_sequence = input().split()
# Save the alphabet in a string and initialise a variable for total sum
alphabet_lower = "".join([chr(x) for x in range(ord('a'), ord('a') + 26)])
total_sum = []
# 12/1=12, 12+2=14, 17*19=323, 323–7=316, 14+316=330
for string in string_sequence:
    first_letter = string[:1]
    last_letter = string[-1:]
    number = int(string[1:-1])
    first_letter_alphabet = alphabet_lower.index(first_letter.lower()) + 1
    last_letter_alphabet = alphabet_lower.index(last_letter.lower()) + 1
    if first_letter.isupper():
        number /= first_letter_alphabet
    elif first_letter.islower():
        number *= first_letter_alphabet
    if last_letter.isupper():
        number -= last_letter_alphabet
    elif last_letter.islower():
        number += last_letter_alphabet
    total_sum.append(number)

print(f'{sum(total_sum):.2f}')
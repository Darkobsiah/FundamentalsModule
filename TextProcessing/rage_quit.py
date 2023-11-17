series = [x for x in input()]
output_line = ''
last_symbol = ''

# Loop through the string
counter = 1
for character in series:
    if character.isnumeric():
        continue
    current_string = ''
    multiplication_number = 1
    # alphabetic character
    if character.isalpha():
        for letter in range(counter, len(series)):
            if series[letter].isalpha():
                current_string += series[letter]
            else:
                multiplication_number = int(series[letter])
                break
    output_line += character.upper() * multiplication_number
    counter += 1

print(f'Unique symbols used: {len(set(output_line))}')
print(output_line)
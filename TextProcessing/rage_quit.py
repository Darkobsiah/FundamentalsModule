from datetime import datetime
start = datetime.now()
series = [x for x in input()]
output_line = ''
last_symbol = ''

# Loop through the string
for character in series:
    # Do not entry non-numeric and symbols who are already in the output
    if character.isnumeric() or character in output_line:
        continue
    current_string = ''
    multiplication_number = 1
    # alphabetic character
    if not character.isnumeric():
        current_string += character
        is_failed = False
        current_index = series.index(current_string)
        while not is_failed:
            for x in range(1, 100):
                if not series[current_index + x].isnumeric():
                    current_string += series[current_index + x]
                else:
                    multiplication_number = int(series[current_index + x])
                    is_failed = True
                    break
        output_line += current_string.upper() * multiplication_number

# Print User output
print(f'Unique symbols used: {len(set(output_line))}')
print(output_line)
end = datetime.now()
print(end - start)
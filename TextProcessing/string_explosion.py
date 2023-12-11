# Read User input
text = input()
power_points = 0
final_output = ''

# Initialise a for loop
for character in range(len(text)):
    # explosion mark
    if text[character] == '>':
        power_points += int(text[character + 1])
        final_output += '>'
    else:
        if power_points > 0:
            # explosion time
            power_points -= 1
        else:
            final_output += text[character]

# Print the output
print(final_output)
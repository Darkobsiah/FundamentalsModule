# Read User input
text = input()
final_message = ""
last_added_character = ""

# Loop through the string
for current_character in text:
    if current_character != last_added_character:
        final_message += current_character
        last_added_character = current_character

# Print User output
print(final_message)

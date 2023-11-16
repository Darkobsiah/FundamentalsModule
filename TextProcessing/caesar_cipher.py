# Read User input
text = input()

# Logic
encrypted_text = ''
for symbol in text:
    encrypted_text += chr(ord(symbol) + 3)

# Print User output
print(encrypted_text)

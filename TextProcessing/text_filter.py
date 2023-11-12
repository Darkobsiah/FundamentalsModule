# Read User input
banned_words = input().split(', ')
text = input()

# Initialise a for loop
for word in banned_words:
    # Initialise a nested while loop
    while word in text:
        # replace banned words within the text
        text = text.replace(word, '*' * len(word))

# Print User output
print(text)

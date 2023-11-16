# Read User input
text = input()

# Logic
emoticons = []
for symbol in range(len(text)):
    emoticon = ':'
    if text[symbol] == ':':
        emoticon += text[symbol + 1]
        emoticons.append(emoticon)

# Print the
print('\n'.join(emoticons))
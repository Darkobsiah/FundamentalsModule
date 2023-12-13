# In case they are separated with [', '] use:
# words = input().split(', ')


# Take the words [every one from a single row]

words = []
word = input()
while word:
    words.append(word)
    word = input()

# find every character from the alphabet
alphabet = [chr(x) for x in range(97, 97 + 26)]
print(alphabet)

letter = 1
while letter < 26:
    words_startswith = []
    for word in words:
        if word.startswith(alphabet[letter]):
            words_startswith.append(word)
    if words_startswith:
        print(f'All the words starting with {alphabet[letter]:}')
        print(f'{", ". join(words_startswith)}')
        print()
    letter += 1

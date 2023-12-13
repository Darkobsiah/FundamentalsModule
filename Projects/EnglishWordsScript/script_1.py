# Initialise a file to save the data
words = []
# Read the data from the text file
data = open('text_data/list_of_words.txt', 'r')
# Append the data into a list
for d in data:
    if '\n' in d:  # Removes new lines
        d = d.replace('\n', '')
    words.append(d)
print(words)


# find every character from the alphabet
alphabet = [chr(x) for x in range(97, 97 + 26)]
print(alphabet)


# Operations with the output
letter = 0
while letter < 26:
    words_startswith = []
    print(f'Current letter: {alphabet[letter]}')
    # Loop through the list
    for word in words:
        if word.startswith(alphabet[letter]):  # if match
            print(f'Word or a phrase found: {word}')

            # Write a sentence into the sentences txt
            file = open('text_data/sentences_list.py', 'w')

            sentence = input('Show imagination: ')
            file.write(sentence)
            file.close()

            # Remove the word from the words list.txt
            f = open('text_data/list_of_words.txt', 'r')
            text = f.read()
            text = text.replace(word, '')
            f.close()
            f = open('text_data/list_of_words.txt', 'w')
            f.write(text)
            f.close()

            print('Sentence saved successfully')
            print()
    # if words_startswith:
    #     print(f'All the words starting with {alphabet[letter]:}')
    #     print(f'{", ". join(words_startswith)}')
    #     print()
    letter += 1

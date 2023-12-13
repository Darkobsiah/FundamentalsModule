def write():
    file = open('sentences.txt', 'w')

    sentence = input('Show imagination: ')
    file.write(sentence)
    file.close()


def remove_words():
    pass


# Initialise a file to save the data
words = []
# Read the data from the text file
data = open('words.txt', 'r')
# Append the data into a list
for d in data:
    if '\n' in d:  # Removes new lines
        d = d.replace('\n', '')
    words.append(d)
print(words)

for word in words:
    print(f'{word}')
    write()
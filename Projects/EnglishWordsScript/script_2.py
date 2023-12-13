def write():
    file = open('text_data/sentences_list.py', 'w')

    sentence = input('Show imagination: ')
    file.write(sentence)
    file.close()


def remove_words():
    pass


# # Initialise a file to save the data
words = []
# # Read the data from the text file
data = open('words_list.txt', 'r')
# # Append the data into a list
data = ['1', '2', '3']
for d in data:
    if '\n' in d:  # Removes new lines
        d = d.replace('\n', '')
    words.append(d)
print(words)

for word in words:
    print(f'{word}')
    write()

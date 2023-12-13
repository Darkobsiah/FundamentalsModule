words = ['pesho', 'nasko', 'dobi', 'slavi']

# while True:
#     words_startswith = []
#     print(f'Current letter: a')
#     # Loop through the list
#     for word in words:
#         if word.startswith('n'):  # if match
#             print(f'Word or a phrase found: {word}')
#
#             # Write a sentence into the sentences txt
file = open('store_data.txt', 'w')
sentences = []
counter = 1
while counter < 3:
    sentence = input('Show imagination: ')
    sentences.append(sentence)
    counter += 1
file.write('\n'.join(sentences))
file.close()

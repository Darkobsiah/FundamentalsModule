words = ['first', 'second', 'third']

for word in words:
    if word.startswith('s'):  # if match
        print(f'Word or a phrase found: {word}')

        # Write a sentence into the sentences.txt
        file = open('sentences.txt', 'w')

        sentence = input('Show imagination: ')
        file.write(sentence)
        file.close()
        print()
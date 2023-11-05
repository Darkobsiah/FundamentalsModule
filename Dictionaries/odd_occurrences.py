sequence_of_words = input().split()

sequence_copy = sequence_of_words.copy()
output_words = []

for word in sequence_of_words:
    if sequence_copy.count(word) % 2 != 0:
        output_words.append(word.lower())
        sequence_copy.remove(word)
        if word.upper() in sequence_copy:
            sequence_copy.remove(word.upper())
        if word.lower() in sequence_copy:
            sequence_copy.remove(word.lower())


for word in output_words:
    print(word,end=' ')
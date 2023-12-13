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

letter = 0
while True:
    for word in words:
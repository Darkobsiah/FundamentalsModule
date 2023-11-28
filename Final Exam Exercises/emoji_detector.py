import re


# Read User input
text = input()

# Calculate the threshold
threshold = 1
number_reg = r"\d"
numbers = re.findall(number_reg, text)
for number in numbers:
    threshold *= int(number)
print(f"Cool threshold: {threshold}")

# Find the length of the emojis
regex = r"([\:|\*]{2})([A-Z][a-z]{2,})\1"
emojis_iterator = re.finditer(regex, text)
# ([\:|\*]{2})[A-Z][a-z]{2,}\1

emojis = []
for e in emojis_iterator:
    emojis.append(e.group())


cool_emojis = []
for emoji in emojis:
    counter = 0
    for letter in emoji:
        if letter.isalpha():
            counter += ord(letter)
    if counter > threshold:
        cool_emojis.append(emoji)

print(f'{len(emojis)} emojis found in the text. The cool ones are:')
for emoji in cool_emojis:
    print(emoji)
import re


text = input()
# Calculate the threshold
threshold = 1
number_reg = r"\d"
numbers = re.findall(number_reg, text)
for number in numbers:
    threshold *= int(number)
print(f"Cool threshold: {threshold}")

# Find the length of the emojis
regex = r"([\::|\**]{2})([A-Z][a-z]{2,})\1"
emojis_count = re.findall(regex, text)


# Find the cool emojis
cool_emojis = []
text = text.split(' ')
for word in text:
    count = 0
    match = re.search(regex, word)
    if match:
        for l in word:
            if l.isalpha():
                count += ord(l)
        if count > threshold:
            cool_emojis.append(word)

print(f'{len(emojis_count)} emojis found in the text. The cool ones are:')
for emoji in cool_emojis:
    if '.' in emoji:
        emoji = emoji.replace('.', '')
    elif ',' in emoji:
        emoji = emoji.replace(',', '')
    print(emoji)
import re


# Read User input
line = input()
word = input()
# Use variable in the regex (?i) - case insensitive
pattern = fr"(?i)\b{word}\b"
result = re.findall(pattern, line)
# Print User output
print(len(result))

import re


text = input()
word = input()
regex = fr"(?i){word}\b"
result = re.findall(regex, text)
print(len(result))
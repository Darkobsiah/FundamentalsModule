import re

text = 'Current year is 2023'
pattern = '\d'
result = re.findall(pattern, text)
print(result)
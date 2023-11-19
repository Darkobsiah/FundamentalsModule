import re

text = 'abc dfb'
pattern = '.'
result = re.findall(pattern, text)
print(result)
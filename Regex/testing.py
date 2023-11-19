import re

text = 'abc def'
pattern = '.'
result = re.findall(pattern, text)
print(result)
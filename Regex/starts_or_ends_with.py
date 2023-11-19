import re

text = 'Python is fun.'
pattern = '^Python'
result = re.findall(pattern, text)
print(result)
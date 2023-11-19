import re

text = 'Python is fun.'
pattern = 'fun\.$'
result = re.findall(pattern, text)
print(result)
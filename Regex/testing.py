import re

text = '1234 123 12 1 12345'
pattern = '\d{3}'
result = re.findall(pattern, text)
print(result)
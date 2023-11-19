import re

text = 'Test this - 50.50'
pattern = '\d+\.\d+'
result = re.findall(pattern, text)
print(result)
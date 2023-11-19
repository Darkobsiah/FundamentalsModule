import re

text = 'This is my cost 50.00'
pattern = '\d+\.\d+'
result = re.findall(pattern, text)
print(result)
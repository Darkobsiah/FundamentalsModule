import re

text = 'The cost is 12.99 leva'
pattern = '\d+\.\d+'
result = re.findall(pattern, text)
print(result)
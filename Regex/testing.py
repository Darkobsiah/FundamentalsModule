import re

text = 'Something3different50.3121'
pattern = '\d+\.\d+'
result = re.findall(pattern, text)
print(result)
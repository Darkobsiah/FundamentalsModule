import re

text = 'hello, hi, hiii, hiiiii'
pattern = 'hi*'
result = re.findall(pattern, text)
print(result)
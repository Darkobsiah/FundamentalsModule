import re

text = 'dog, cat, bird, snake'
pattern = 'dog|cat'
result = re.findall(pattern, text)
print(result)
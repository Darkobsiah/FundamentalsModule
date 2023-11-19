import re

text = 'Python is an interpreted language'
pattern = '[abc]'
result = re.findall(pattern, text)
print(result)
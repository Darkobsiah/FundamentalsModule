import re

text = 'something fun to do is playing football'
pattern = '[abc]'
result = re.findall(pattern, text)
print(result)
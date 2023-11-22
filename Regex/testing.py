import re


regex = r'\b_([A-Za-z0-9]+)\b'
text = input()
result = re.findall(regex, text)
print(' '.join(result))
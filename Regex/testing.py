import re


regex = '\d+'
text = input()
while text:
    match = re.findall(regex, text)
    if match:
        print(' '.join(match),end=' ')
    text = input()
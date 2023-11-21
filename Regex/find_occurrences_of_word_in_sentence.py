import re


line = input()
word = input()
result = re.search(fr'+ word +', line)
print(result)

import re

numbers = input().split(', ')
regex_template = r'\+359([ -])\d{1}\1\d{3}\1\d{4}\b'

valid_numbers = []
for number in numbers:
    result = re.findall(regex_template, numbers)
    if result:
        valid_numbers.append(number)
print(valid_numbers)
import re

text = input()
regex_pattern = r'(\d{2})([-./])([A-Z][a-z]{2})\2(\d{4})'
valid_data = re.findall(regex_pattern, text)

for data in valid_data:
    print(f'Day: {data[0]}, Month: {data[2]}, Year: {data[3]}')


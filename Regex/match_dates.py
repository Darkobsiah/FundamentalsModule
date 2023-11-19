import re

text = input()
regex_pattern = r'(\d{2})([-.\/])([A-Z][a-z]{2})\2(\d{4})'
valid_data = re.findall(regex_pattern, text)

for data in valid_data:
    d = data[0]
    m = data[2]
    y = data[3]
    print(f'Day: {d}, Month: {m}, Year: {y}')

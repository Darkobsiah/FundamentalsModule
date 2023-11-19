import re

text = input()
regex_pattern = r'(\d{2})([-.\/])([A-Z][a-z]{2})\2(\d{4})'
valid_data = re.finditer(regex_pattern, text)

for data in valid_data:
    day = data.group(1)
    month = data.group(3)
    year = data.group(4)
    print(f'Day: {day}, Month: {month}, Year: {year}')

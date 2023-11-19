import re

text = input()
regex_pattern = r'(\d{2})([-.\/])([A-Z][a-z]{2}\2\d{4})'
valid_data = re.findall(regex_pattern, text)

print(valid_data)
for data in valid_data:
    month, year = data[2].split()
    print(f'Day: {data[0]} Month: {data[1]}, Year: {data[2]}')

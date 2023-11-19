import re


numbers = input()

regex_template = r'\+359 \d{1} \d{3} \d{4}\b|\+359-\d{1}-\d{3}-\d{4}\b'
matches = re.findall(regex_template, numbers)

# Print User output
print(matches)
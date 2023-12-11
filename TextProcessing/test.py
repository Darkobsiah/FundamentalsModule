lack = input()
text = input()
while lack in text:
    text = text.replace(lack, '')

print(text)
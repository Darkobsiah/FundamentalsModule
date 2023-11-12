# Read User input
text = input().split()

# initialise a list comprehension
new_text = [txt * len(txt) for txt in text]

# the better variation
print(' '.join(new_text))

# OLD-FASHIONED
# for word in new_text:
#     print(word,end=' ')
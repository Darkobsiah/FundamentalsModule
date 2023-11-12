text = input().split()

new_text = [txt * len(txt) for txt in text]

for word in new_text:
    print(word,end=' ')
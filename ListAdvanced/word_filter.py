some_text = input().split()
even_len_list = []
for word in some_text:
    if len(word) % 2 == 0:
        even_len_list.append(word)

for element in even_len_list:
    print(element)
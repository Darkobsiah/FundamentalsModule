lines = int(input())

my_dict = {}

for _ in range(lines):
    word = input()
    synonym = input()
    if word in my_dict:
        my_dict[word] += f', {synonym}'
    else:
        my_dict[word] = synonym

for key, value in my_dict.items():
    print(f'{key} - {value}')
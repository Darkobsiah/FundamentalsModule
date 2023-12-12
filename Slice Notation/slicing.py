text = 'I love living in the world of Python*'

print('*' * len(text))

print(text[:1:])
print(text[2:7:])
print(text[7:13:])
print(text[14:16:])
print('*-' * (len(text) // 2))
print(f'{text}')
print('*-' * (len(text) // 2))
print(text[-7:-1:])
print(text[-10:-8:])
print(text[-16:-11:])

print('*' * len(text))
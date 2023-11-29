characters = input().split(', ')

ascii_char_representation = [ord(x) for x in characters]

dictionary = dict(zip(characters, ascii_char_representation))

print(dictionary)
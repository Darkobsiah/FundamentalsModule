characters = input().split(', ')

ascii = [ord(x) for x in characters]

output_dict = dict(zip(characters, ascii))
print(output_dict)
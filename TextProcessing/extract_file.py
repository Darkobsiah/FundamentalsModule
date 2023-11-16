
path_locations = input().split('\\')
file_name, extension = path_locations[-1].split('.')

print(f'File name: {file_name}\n'
      f'File extension: {extension}')


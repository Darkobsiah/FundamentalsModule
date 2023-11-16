# Read Whole path and split it by \ escaped by \
path_locations = input().split('\\')
# Take the last part with [-1] and split by '.' to take
# file_name and the extension
file_name, extension = path_locations[-1].split('.')
# Print the output on new line
print(f'File name: {file_name}\n'
      # on new line
      f'File extension: {extension}')


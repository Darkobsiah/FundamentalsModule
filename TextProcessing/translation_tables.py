import string
input_string = """This is PythonForBeginners.com.
Here, you   can read python tutorials for free."""
translation_table = input_string.maketrans("abcdefghijklmnopqrstupwxyz",
"ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print("The translation table is:")
print(translation_table)

print('The string representation is:')
for key, value in translation_table.items():
    print(f'{chr(key)}:{chr(value)}',end='   ')
# Read User input
first_string = input()
second_string = input()

# Initialise a while loop
while first_string in second_string:
    second_string = second_string.replace(first_string, '')

# Print User output
print(second_string)
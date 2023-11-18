# Read User input
string_sequence = input().split()
# Save the alphabet in a string and initialise a variable for total sum
alphabet_lower = "".join([chr(x) for x in range(ord('a'), ord('a') + 26)])
total_sum = []

for string in string_sequence:
    first_letter = string[:1]
    last_letter = string[-1:]
    number = string[1:-1]

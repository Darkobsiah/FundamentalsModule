# Read User input
first_s, second_s = input().split()
total_sum = 0
if len(first_s) > len(second_s):
    for letter in range(len(second_s)):
        total_sum += ord(first_s[letter]) * ord(second_s[letter])
    diff = len(first_s) - len(second_s)
    for let in range(len(first_s) - diff, len(first_s)):
        total_sum += ord(first_s[let])
elif len(first_s) < len(second_s):
    for letter in range(len(second_s)):
        total_sum += ord(first_s[letter]) * ord(second_s[letter])
    diff = len(first_s) - len(second_s)
    for let in range(len(first_s) - diff, len(first_s)):
        total_sum += ord(first_s[let])
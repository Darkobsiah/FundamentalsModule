def add_multiplied_nums(sum: int, first: str, second: str) -> int:
    """
    This function multiplies the asci representation of the
    letter - len(shorter_word) times. Then takes the remaining
    letter of the longer string and add their ord() in the sum.
    """
    shorter = second
    longer = first
    if len(first) < len(second):
        shorter = first
        longer = second
    for letter in range(len(shorter)):
        sum += ord(first[letter]) * ord(second[letter])
        # the len difference of the strings
        diff = len(second_s) - len(first_s)
        # add the sum of the left letters in the longer string
        for let in range(len(second_s) - diff, len(second_s)):
            sum += ord(second_s[let])
    return sum


# Read User input
first_s, second_s = input().split()
total_sum = 0

if len(first_s) > len(second_s):
    total_sum += add_multiplied_nums(total_sum, first_s, second_s)
    diff = len(first_s) - len(second_s)

elif len(first_s) < len(second_s):
    total_sum += add_multiplied_nums(total_sum, first_s, second_s)
    diff = len(second_s) - len(first_s)

else:   # when the string has the same length
    total_sum += add_multiplied_nums(total_sum, first_s, second_s)
print(total_sum)
import re

string = input()
cool_threshold_sum = 1
emoji_is_cool = []
pattern_digit = r"\d"
match_digit = re.findall(pattern_digit, string)
for current_digit in match_digit:
    cool_threshold_sum *= int(current_digit)

pattern_emoji = r"::[A-Z][a-z]{2,}::|\*\*[A-Z][a-z]{2,}\*\*"
match_emoji = re.findall(pattern_emoji, string)
for current_emoji in match_emoji:
    total_ascii_letter = 0
    for letter in current_emoji:
        if letter.isalpha():
            total_ascii_letter += ord(letter)
    if total_ascii_letter >= cool_threshold_sum:
        emoji_is_cool.append(current_emoji)

print(f"Cool threshold: {cool_threshold_sum}")
print(f"{len(match_emoji)} emojis found in the text. The cool ones are:")
for cool_emoji in emoji_is_cool:
    print(cool_emoji)
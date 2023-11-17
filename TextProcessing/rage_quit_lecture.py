text = input()
unique_symbols = ""
repetitions = ""
current_symbol = ""
for index in range(len(text)):
    if not text[index].isdigit():  # We have non-numeric character
        current_symbol += text[index]
    else:  # We have digits here -> time for repetition
        ...
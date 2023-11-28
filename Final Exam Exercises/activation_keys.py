# Read User input
raw_key = input()

# Logic
while True:
    command = input()
    if command == "Generate":
        break

    command = command.split(">>>")
    if command[0] == "Contains":
        pass
    elif command[0] == "Flip":
        if command[1] == "Upper":
            pass
        elif command[1] == "Lower":
            pass
    elif command[0] == "Slice":
        pass


# Print User output
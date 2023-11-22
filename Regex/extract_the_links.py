import re


regex = r"(w{3}.[A-Za-z0-9-]+(\.[a-z]+)+)"
command = input()
while True:
    if command:
        link = re.search(regex, command)
        if link:
            print(link.group(0))
    else:
        break
    command = input()

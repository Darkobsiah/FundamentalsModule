names = ['John', 'Den','Mark', 'Jane']

print(sorted(names, key = lambda name: name.split()[-1]))



c = input('replace: ')
r = input('with: ')
f = open('sentences.txt', 'r')
text = f.read()
text = text.replace(c, r)
f.close()

f = open('sentences.txt', 'w')
f.write(text)
f.close()


# open the file
# read the file
# replace the word
# close it

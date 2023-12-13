
c = input('replace: ')
r = input('with: ')
f = open('text_data/sentences_list.py', 'r')
text = f.read()
text = text.replace(c, r)
f.close()

f = open('text_data/sentences_list.py', 'w')
f.write(text)
f.close()


# open the file
# read the file
# replace the word
# close it

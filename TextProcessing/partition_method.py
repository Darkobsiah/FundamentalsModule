text = 'blabla,#how are you today'

if '#' in text:
    try:
        text = text.partition('#')
        print('Successfully found result!')
        print(f"L -> {text[0]}")
        print(f"separator -> {text[1]}")
        print(f"R -> {text[2]}")
    except:
        print('Error 404')

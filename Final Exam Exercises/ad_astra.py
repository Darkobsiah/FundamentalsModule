item_credentials = {}

text = '#Bread#19/03/21#4000#|Invalid|03/03.20||Apples|' \
       '08/10/20|200||Carrots|06/08/20|500||Not right|6.8.20|5|'

text = text.split('#')
item_credentials[text[1]] = {'expiration_date': text[2],
                             'calories': text[3]}
print(item_credentials)
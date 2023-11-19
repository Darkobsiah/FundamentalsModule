import re

email_date = ['valid123@email.bg', 'invalid*name@email.bg']

pattern = r'^[a-zA-Z0-9]+@+[a-zA-Z]+\.[a-zA-Z]'

for email in email_date:
    if re.match(pattern, email):
        print(email)
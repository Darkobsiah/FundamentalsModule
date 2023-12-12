import requests

payload = {'username': 'Zazi', 'password': 'text'}
r = requests.post('https://httpbin.org/post', data=payload)

r_dict = r.json()
for key, value in r_dict.items():
    print(f'{key} -> {value}')

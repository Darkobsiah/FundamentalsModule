import requests

r = requests.get('https://httpbin.org/basic-auth/slavi/testing', auth=('slavi', 'testing'))

print(r.text)
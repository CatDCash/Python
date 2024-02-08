import requests

res = requests.get('http://catdcash.github.io')

print(res.text)
print(res.status_code)

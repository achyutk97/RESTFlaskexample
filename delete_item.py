import requests

response = requests.delete(url="http://127.0.0.1:5000/drinks/1")
print(response.text)
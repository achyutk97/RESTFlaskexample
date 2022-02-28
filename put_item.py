import requests

data = {
    'name': 'juice',
    'description': 'it\'s like hot'
}

response = requests.put('http://127.0.0.1:5000/drinks/2', json=data)
print(response.text)
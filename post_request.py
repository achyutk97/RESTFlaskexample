import requests

data = {
    'name': 'cola',
    'description': 'take like 7up'
}

response = requests.post('http://127.0.0.1:5000/drinks', json=data)
print(response.text)
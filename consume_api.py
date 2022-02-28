import requests

response = requests.get("http://127.0.0.1:5000/drinks")

for data in response.json()['drinks']:
    print(data['name'], "--->" , data['description'])
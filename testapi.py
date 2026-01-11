import requests
import json

# url = "http://0.0.0.0:5000/users"
url = "http://192.168.1.4:5000/users"
headers = {
  'Content-Type': 'application/json'
}

response = requests.get(url, headers=headers)
print(response.text)
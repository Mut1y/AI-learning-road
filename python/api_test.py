import requests


url = "https://api.github.com"
response = requests.get(url, timeout=10)
response.raise_for_status()

data = response.json()
print(data)

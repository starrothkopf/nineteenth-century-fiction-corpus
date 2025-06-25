import requests

params = {
    "topic": "short stories",
    "languages": "en",
    "copyright": "false",
    "min_year": 1789,
    "max_year": 1913,
}

response = requests.get("http://127.0.0.1:8000/books/", params=params)
data = response.json()
print(data["results"])
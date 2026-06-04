import requests

url = "http://127.0.0.1:5000/update"

payload = {
    "component": "Arduino-Uno",
    "confidence": 92.5
}

response = requests.post(
    url,
    json=payload
)

print(response.json())
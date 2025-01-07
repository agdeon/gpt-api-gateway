import requests

url = "https://127.0.0.1:8000/api/v1/gpt/chat"
data = {
    "name": "Andrew1",
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=data, headers=headers, verify=False)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code}, {response.text}")
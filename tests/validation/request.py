import requests

# - user_id
# - API_KEY
# - chat_completions_creation_obj:
# 	{
# 			model: "gpt-4o-mini",
# 			messages: [{ role: "user", content: "Just say this is a test" }],
# 			temperature
# 			top_p
# 	}

url = "https://127.0.0.1:8000/api/v1/gpt/chat"
data = {
    "user_id": "3131213",
    "api_key": "adfalskjflaskfas",
    "chat_completions_creation_obj": {
        "model": "gpt-4o-mini",
        "messages": [{ "role": "user", "content": "Just say this is a test" }],
    }
}

headers = {
    "Content-Type": "application/json"
}

response = requests.post(url, json=data, headers=headers, verify=False, timeout=30)

if response.status_code == 200:
    print(response.json())
else:
    print(f"Error: {response.status_code}, {response.text}")
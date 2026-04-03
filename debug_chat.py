import requests

url = "http://127.0.0.1:10001/chat"
payload = {
    "query": "benefits?",
    "scheme": None,
    "user_profile": {}
}

response = requests.post(url, json=payload)
print(f"Status: {response.status_code}")
print(f"Response: {response.json()}")

# Malformed scheme (list instead of dict)
payload["scheme"] = [{"scheme_name": "Test"}]
response = requests.post(url, json=payload)
print(f"Status: {response.status_code}")
print(f"Response: {response.json()}")

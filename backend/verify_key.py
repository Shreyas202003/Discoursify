import requests
import json

API_KEY = "AIzaSyCU0yC4GSJHuyIvtoHCnPfw4P201RR2q9E"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key={API_KEY}"

headers = {"Content-Type": "application/json"}
data = {
    "contents": [{
        "parts": [{"text": "Say Hello"}]
    }]
}

try:
    response = requests.post(URL, headers=headers, json=data)
    print(f"Status Code: {response.status_code}")
    print(f"Response: {response.text}")
except Exception as e:
    print(f"Error: {e}")

import urllib.request
import json
import ssl
import os

# Token provided by user
TOKEN = os.getenv("GITHUB_TOKEN")
ENDPOINT = "https://models.inference.ai.azure.com/chat/completions"
MODEL_NAME = "gpt-4o"

def test_github_model():
    print(f"Testing GitHub Model: {MODEL_NAME}")
    print(f"Endpoint: {ENDPOINT}")
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {TOKEN}"
    }
    
    payload = {
        "messages": [
            {
                "role": "user",
                "content": "Hello, are you working?"
            }
        ],
        "model": MODEL_NAME,
        "temperature": 1.0,
        "max_tokens": 100,
        "top_p": 1.0
    }
    
    try:
        req = urllib.request.Request(ENDPOINT, data=json.dumps(payload).encode('utf-8'), headers=headers)
        context = ssl._create_unverified_context()
        
        with urllib.request.urlopen(req, context=context) as response:
            status = response.getcode()
            body = response.read().decode('utf-8')
            print(f"Status: {status}")
            print(f"Response: {body}")
            
    except urllib.error.HTTPError as e:
        print(f"HTTP Error: {e.code} - {e.reason}")
        print(f"Error Body: {e.read().decode('utf-8')}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_github_model()

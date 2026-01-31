import urllib.request
import json
import ssl

API_KEY = "AIzaSyCU0yC4GSJHuyIvtoHCnPfw4P201RR2q9E"
URL = f"https://generativelanguage.googleapis.com/v1beta/models?key={API_KEY}"

try:
    with open("models.log", "w") as f:
        f.write("Available Models:\n")
        context = ssl._create_unverified_context()
        
        with urllib.request.urlopen(URL, context=context) as response:
            data = json.loads(response.read().decode('utf-8'))
            
            for model in data.get('models', []):
                if 'generateContent' in model.get('supportedGenerationMethods', []):
                    f.write(f"- {model['name']}\n")
    print("Done writing to models.log")
            
except Exception as e:
    print(f"Script Error: {e}")

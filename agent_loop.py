import requests
import os

HF_TOKEN = os.getenv("HF_API_TOKEN")
API_URL = "https://api-inference.huggingface.co/models/deepseek-ai/deepseek-coder-33b-instruct"

headers = {"Authorization": f"Bearer {HF_TOKEN}"}

def query(payload):
    response = requests.post(API_URL, headers=headers, json=payload)
    
    print(f"Status Code: {response.status_code}")
    if response.status_code != 200:
        raise Exception(f"Request failed with status code {response.status_code}: {response.text}")
    
    return response.json()

prompt = "Explain Python recursion."

result = query({
    "inputs": prompt,
    "parameters": {"max_new_tokens": 512}
})

print(result)

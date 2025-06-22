import requests
import json

class OllamaBackend:
    def __init__(self, model="mistral"):
        self.model = model

    def ask(self, prompt):
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": self.model, "prompt": prompt},
            stream=True
        )
        response.raise_for_status()
        
        if response.status_code != 200: # Check for successful response
            raise Exception(f"Request failed with status code {response.status_code}: {response.text}")
        
        output = ""
        for line in response.iter_lines():
            if line:
                try:
                    data = json.loads(line.decode("utf-8"))
                    chunk = data.get("response", "")
                    print(chunk, end="", flush=True)  # <== show output while waiting
                    output += chunk
                except json.JSONDecodeError:
                    pass  # Skip broken chunks
        print()
        return output.strip()


# Note: This is a simplified version of the loop without agents.
# In a real application, you would likely have more structured error handling,
# logging, and possibly more complex interactions between agents.
# This example is meant to illustrate the basic flow of asking a model for code generation and review.
# Make sure to have the Ollama server running locally for this to work.

# Ensure you have the necessary permissions and environment set up to run this code.
# This code assumes you have the Ollama server running locally and the model "mistral" available.
# Adjust the model name as needed based on your setup.

# Install Ollama if not already installed
# >curl https://ollama.com/install.sh | bash
# >ollama --version

# check if Ollama is running
# >ps aux | grep -i ollama

# If Ollama is not running, start Ollama
# >ollama serve

# Then, pull the Mistral model
# >ollama pull mistral

# You can run this script directly to see the interaction with the Ollama backend.
# Make sure to have the necessary packages installed:
# pip install requests

# This code is a simplified version of the agent loop, focusing on local CPU execution.
# It does not include advanced error handling or logging, which would be important in a production scenario.
# The code is designed to be run in a local environment where the Ollama server is accessible.

# python examples/local_cpu_loop_simple.py

# Ensure you have the Ollama server running and the model "mistral" available for testing.
# This example is meant to illustrate the basic flow of asking a model for code generation and review.
# You can extend this code to include more complex interactions, such as multiple iterations of writing, reviewing, and testing code.
# The code is structured to be easily readable and maintainable,
# allowing for future enhancements and modifications as needed.

import requests
import json

# === Simple backend function ===
def ask_ollama(model, prompt):
    response = requests.post(
        "http://localhost:11434/api/generate",
        json={"model": model, "prompt": prompt},
        stream=True
    )
    response.raise_for_status()

    output = ""
    for line in response.iter_lines():
        if line:
            data = json.loads(line.decode("utf-8"))
            chunk = data.get("response", "")
            print(chunk, end="", flush=True)  # Show output live
            output += chunk

    print()  # Newline after done
    return output.strip()

# === Main flow ===
if __name__ == "__main__":
    model = "mistral"

    # Writer step
    task = "Write a Python function to compute Fibonacci numbers."
    print("\n[Writer] Asking...")
    code_output = ask_ollama(model, task)

    # Reviewer step
    review_prompt = f"Please review the following Python code and provide suggestions:\n\n{code_output}"
    print("\n[Reviewer] Asking...")
    review_output = ask_ollama(model, review_prompt)

    # Tester step (optional)
    # Here we could add a testing step if needed, but for simplicity, we'll skip it
    # Note: In a real scenario, you might want to implement a testing agent here   
    test_prompt = f"Write pytest test cases for the following Python function:\n\n{code_output}"
    print("\n[Tester] Asking...")
    test_output = ask_ollama(model, test_prompt)

    # Final print
    print("\n=== Final Review ===")
    print(review_output)

    print("\n=== Final Tests ===")
    print(test_output)
    
    
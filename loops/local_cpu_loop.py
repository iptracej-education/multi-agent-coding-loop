from backends.ollama_backend import OllamaBackend
from agents.writer_agent import WriterAgent
from agents.reviewer_agent import ReviewerAgent
from agents.tester_agent import TesterAgent 

if __name__ == "__main__":
    backend = OllamaBackend(model="mistral")
    writer = WriterAgent(backend)
    reviewer = ReviewerAgent(backend)
    tester = TesterAgent(backend)

    # Simple task
    task = "Write a Python function to compute Fibonacci numbers."
    code_output = writer.run(task)
    
    review_output = reviewer.run(code_output)

    test_output = tester.run(code_output)

    print("\n=== Final Review ===")
    print(review_output)
    
    print("\n=== Final Tests ===")
    print(test_output)
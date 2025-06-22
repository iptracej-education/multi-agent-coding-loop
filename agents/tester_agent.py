class TesterAgent:
    def __init__(self, backend):
        self.backend = backend

    def run(self, code_output):
        test_prompt = f"Write pytest test cases for the following Python function:\n\n{code_output}"
        print(f"\n[TesterAgent] Generating tests...")
        test_output = self.backend.ask(test_prompt)
        print(f"\n[TesterAgent] Tests complete.")
        return test_output

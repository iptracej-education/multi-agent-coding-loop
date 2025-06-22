# Placeholder for agents/reviewer_agent.py
class ReviewerAgent:
    def __init__(self, backend):
        self.backend = backend

    def run(self, code_output):
        review_prompt = f"Please review the following Python code and provide suggestions to improve it:\n\n{code_output}"
        print(f"\n[ReviewerAgent] Reviewing the code...")
        review = self.backend.ask(review_prompt)
        print(f"\n[ReviewerAgent] Review complete.")
        return review  
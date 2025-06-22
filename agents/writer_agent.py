class WriterAgent:
    def __init__(self, backend):
        self.backend = backend

    def run(self, task):
        print(f"[WriterAgent] Task: {task}")
        output = self.backend.ask(task)
        print(f"[WriterAgent] Output:\n{output}")
        return output

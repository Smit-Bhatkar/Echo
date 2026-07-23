import ollama

class Brain:
    def __init__(self, model="qwen3:4b"):
        self.model = model
        self.messages = [
            {
                "role": "system",
                "content": (
                    "You are Echo, a personal AI assistant. "
                    "Be concise, helpful and friendly."
                )
            }
        ]

    def ask(self, prompt):
        self.messages.append({"role": "user", "content": prompt})

        response = ollama.chat(
            model=self.model,
            messages=self.messages
        )

        answer = response["message"]["content"]

        self.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        return answer
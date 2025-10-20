import openai

from fastpaip_app.classifications.domain.ports import LLMClassifier


class OpenAIClassifier(LLMClassifier):
    """
    A concrete adapter that implements the 'CanClassify' port
    using the OpenAI API.
    """
    def __init__(self, api_key: str, model: str = "gpt-4"):
        self.client = openai.OpenAI(api_key=api_key)
        self.model = model

    def classify(self, data: str) -> dict:
        """Uses the OpenAI API to classify the given text."""
        print("INFRASTRUCTURE (OpenAI): Classifying text...")
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "You are a helpful assistant that classifies text into categories like 'sales' or 'support'."},
                {"role": "user", "content": data},
            ]
        )
        # In a real app, you would parse the response more robustly.
        classification = response.choices[0].message.content
        return {"category": classification}
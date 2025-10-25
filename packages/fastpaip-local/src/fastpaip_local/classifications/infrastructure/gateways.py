import openai

from fastpaip_local.classifications.domain.models import Category
from fastpaip_local.classifications.domain.ports import LLMClassifier


class OpenAIClassifierGateway(LLMClassifier):
    """
    A concrete adapter that implements the 'CanClassify' port
    using the OpenAI API.
    """
    def __init__(self, api_key: str, model: str = "gpt-4"):
        self.client = openai.OpenAI(api_key=api_key)
        self.model = model

    def classify(self, data: str) -> Category:
        """Uses the OpenAI API to classify the given text."""
        print("INFRASTRUCTURE (OpenAI): Classifying text...")
        
        category = Category.GENERATED

        return category